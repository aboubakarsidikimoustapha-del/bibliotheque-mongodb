"""Connexion à MongoDB (Atlas ou local) partagée par toute l'application."""
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()  # charge le fichier .env en local ; sur Vercel, les variables viennent du dashboard

MONGODB_URI = os.environ.get("MONGODB_URI")
if not MONGODB_URI:
    raise RuntimeError("La variable d'environnement MONGODB_URI est manquante.")

# Le client est créé UNE SEULE FOIS au chargement du module (important en serverless :
# il est réutilisé tant que la fonction reste "chaude").
client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
db = client["bibliotheque"]
livres = db["livres"]
