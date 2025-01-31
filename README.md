# 🔧 DIY Project Generator

Ce projet permet de générer des **idées de projets DIY (Do It Yourself)** avec des tutoriels détaillés, la possibilité de les **enregistrer en PDF**, et d'ajouter des **favoris**.

## 🚀 Fonctionnalités
✅ Génération d'idées de projets DIY  
✅ Création automatique de tutoriels détaillés (GPT-4)  
✅ Téléchargement des tutoriels en PDF  
✅ Système de favoris  
✅ Interface web interactive  

---

## 📦 Installation

### 1️⃣ Cloner le projet  
```bash
git clone https://github.com/tucommenceapousser/diypropose
cd diypropose
```

2️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

3️⃣ Créer le fichier .env

Dans ton dossier principal, crée un fichier .env et ajoute :

```json
OPENAI_API_KEY=ta_cle_openai
```

4️⃣ Initialiser la base de données

```bash
python database.py
```

5️⃣ Lancer le serveur

```bash
python app.py
```

---

🎮 Utilisation

Accède à l’application sur http://127.0.0.1:5000/

Clique sur "Obtenir une Idée" pour générer un projet

Génère un tutoriel détaillé

Télécharge le PDF ou ajoute aux favoris



---

📌 Améliorations futures

Ajout de catégories de projets

Filtrage par niveau de difficulté

Intégration d'images générées par DALL-E



---

💡 Un projet de bricolage fun et interactif ! 🔥
