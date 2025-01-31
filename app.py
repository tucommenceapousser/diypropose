from flask import Flask, render_template, request, jsonify
import sqlite3
import openai
from fpdf import FPDF
import os
import config  # Import de la configuration

app = Flask(__name__)

# Utilisation de la clé OpenAI depuis config.py
openai.api_key = config.OPENAI_API_KEY

# Fonction pour générer une idée de projet
def generer_idee():
    prompt = "Donne-moi une idée de projet DIY original."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Fonction pour générer un tutoriel détaillé
def generer_tutoriel(projet):
    prompt = f"Crée un tutoriel détaillé pour un projet DIY sur {projet}.\
    Structure-le ainsi :\
    - Matériel nécessaire\
    - Étapes détaillées\
    - Conseils pratiques\
    - Lien vers une vidéo YouTube"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

# Route : Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route : Obtenir une idée de projet
@app.route('/get_idea', methods=['GET'])
def get_idea():
    idee = generer_idee()
    return jsonify({"idee": idee})

# Route : Générer un tutoriel
@app.route('/generer_tutoriel', methods=['POST'])
def generer_tutoriel_route():
    projet = request.form.get('projet')
    
    if projet:
        tutoriel = generer_tutoriel(projet)
        
        conn = sqlite3.connect("data/diy.db")
        c = conn.cursor()
        c.execute('''
        INSERT OR REPLACE INTO tutoriels (titre, description, materiel, etapes, conseils, video_url, pdf_url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (projet, tutoriel, "À compléter", "À compléter", "À compléter", "À compléter", ""))
        
        conn.commit()
        conn.close()

        return jsonify({"tutoriel": tutoriel})
    
    return jsonify({"error": "Aucun projet spécifié"})

# Fonction : Générer un PDF
def generer_pdf(projet, contenu):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, projet, ln=True, align='C')
    
    for ligne in contenu.split("\n"):
        pdf.multi_cell(0, 10, ligne)

    pdf_path = f"static/pdfs/{projet.replace(' ', '_')}.pdf"
    pdf.output(pdf_path)
    return pdf_path

# Route : Télécharger le tutoriel en PDF
@app.route('/telecharger_pdf', methods=['POST'])
def telecharger_pdf():
    projet = request.form.get('projet')

    if projet:
        conn = sqlite3.connect("data/diy.db")
        c = conn.cursor()
        c.execute("SELECT description FROM tutoriels WHERE titre = ?", (projet,))
        data = c.fetchone()
        conn.close()
        
        if data:
            pdf_path = generer_pdf(projet, data[0])
            return jsonify({"pdf_url": pdf_path})
    
    return jsonify({"error": "Aucun tutoriel trouvé"})

# Route : Ajouter un favori
@app.route('/ajouter_favori', methods=['POST'])
def ajouter_favori():
    projet = request.form.get('projet')

    if projet:
        conn = sqlite3.connect("data/diy.db")
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO favoris (titre) VALUES (?)", (projet,))
        conn.commit()
        conn.close()
        return jsonify({"success": "Ajouté aux favoris"})
    
    return jsonify({"error": "Erreur d'ajout"})

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
