TP3 – Catalogue de la bibliothèque

Application web de gestion d’un catalogue de bibliothèque développée avec Python, Flask et MongoDB Atlas, puis déployée sur Vercel.

🌐 Application en ligne

👉 Accéder à l'application :
https://bibliotheque-mongodb-phi.vercel.app/

📋 Description

Ce projet consiste à développer une application web permettant de gérer un catalogue de livres à l'aide d'une base de données MongoDB.

L'application permet notamment de :

- consulter les livres disponibles ;
- ajouter un livre ;
- modifier les informations d'un livre ;
- supprimer un livre ;
- rechercher des livres ;
- manipuler les données stockées dans MongoDB Atlas.

🛠️ Technologies utilisées

- Python
- Flask
- MongoDB
- MongoDB Atlas
- PyMongo
- Vercel
- HTML / CSS

📁 Structure du projet

.
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
│   └── ...
└── README.md

⚙️ Installation

1. Cloner le projet

git clone <URL_DU_DEPOT>
cd <NOM_DU_PROJET>

2. Créer un environnement virtuel

python -m venv .venv

Windows :

.venv\Scripts\activate

Linux / macOS :

source .venv/bin/activate

3. Installer les dépendances

pip install -r requirements.txt

4. Configurer MongoDB Atlas

Copier le fichier ".env.example" vers ".env" :

cp .env.example .env

Puis renseigner l'URI de connexion MongoDB Atlas :

MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/

⚠️ Remplacer les valeurs par celles de votre propre base MongoDB Atlas.

Ne jamais publier le fichier ".env" sur GitHub.

▶️ Lancement en local

Lancer l'application avec :

python app.py

Puis ouvrir :

http://127.0.0.1:5000

☁️ Déploiement

L'application est déployée sur Vercel et utilise MongoDB Atlas comme base de données.

URL de production

https://bibliotheque-mongodb-phi.vercel.app/

🔐 Sécurité

Les informations de connexion à MongoDB doivent rester confidentielles.

Le fichier ".env" doit être exclu du dépôt Git :

.env
.venv/
__pycache__/
*.pyc

📝 Travail demandé

Le projet est réalisé dans le cadre du TP3 MongoDB.

Les fonctionnalités et opérations demandées dans l'énoncé du TP doivent être implémentées et testées dans l'application.

👤 Auteur

Aboubakar Sidiki Moustapha

Projet réalisé dans le cadre des travaux pratiques sur MongoDB et Python.