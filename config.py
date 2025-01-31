import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Récupérer la clé API OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
