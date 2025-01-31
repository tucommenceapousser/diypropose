from flask import Flask, render_template, request, jsonify
import openai
import sqlite3
from config import OPENAI_API_KEY

app = Flask(__name__)

# Configuration OpenAI
openai.api_key = OPENAI_API_KEY

# 📌 Fonction pour générer des idées de projets DIY
def generer_idees_diy(preferences):
    prompt = f"Donne-moi 5 idées de projets DIY en rapport avec {preferences}. Chaque projet doit inclure un titre et une courte description."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# 📌 Route de l’accueil
@app.route('/')
def index():
    return render_template('index.html')

# 📌 Route pour rechercher des idées
@app.route('/rechercher', methods=['POST'])
def rechercher():
    preferences = request.form.get('preferences')
    if preferences:
        idees = generer_idees_diy(preferences)
        return jsonify({"idees": idees})
    return jsonify({"error": "Aucune préférence fournie"})

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
