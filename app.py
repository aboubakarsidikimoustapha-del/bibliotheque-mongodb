"""API + page web du catalogue de la bibliothèque (Flask + PyMongo)."""
from bson import ObjectId
from bson.errors import InvalidId
from flask import Flask, jsonify, render_template, request

from db import livres

app = Flask(__name__)


def serialiser(doc):
    """Transforme un document MongoDB en dictionnaire compatible JSON (ObjectId -> str)."""
    doc["_id"] = str(doc["_id"])
    return doc


def vers_object_id(id_str):
    try:
        return ObjectId(id_str)
    except InvalidId:
        return None


@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/api/sante")
def sante():
    """Vérifie que l'application et la base répondent."""
    return jsonify({"statut": "ok", "livres": livres.count_documents({})})


# ---------- READ ----------
@app.route("/api/livres", methods=["GET"])
def lister_livres():
    filtre = {}
    genre = request.args.get("genre")
    if genre:
        filtre["genre"] = genre
    if request.args.get("disponible") == "true":
        filtre["disponible"] = True
    docs = [serialiser(d) for d in livres.find(filtre).sort("titre", 1)]
    return jsonify(docs)


@app.route("/api/livres/<id>", methods=["GET"])
def obtenir_livre(id):
    oid = vers_object_id(id)
    if oid is None:
        return jsonify({"erreur": "identifiant invalide"}), 400
    doc = livres.find_one({"_id": oid})
    if doc is None:
        return jsonify({"erreur": "livre introuvable"}), 404
    return jsonify(serialiser(doc))


# ---------- CREATE ----------
@app.route("/api/livres", methods=["POST"])
def creer_livre():
    donnees = request.get_json(silent=True) or {}

    if not donnees.get("titre"):
        return jsonify({"erreur": "titre requis"}), 400

    if "disponible" not in donnees:
        donnees["disponible"] = True

    resultat = livres.insert_one(donnees)

    return jsonify({"insertedId": str(resultat.inserted_id)}), 201
    # TODO Q3.3 :
    #  1. Si "titre" est absent -> renvoyer {"erreur": "..."} avec le code 400
    #  2. Ajouter disponible=True par défaut si le champ est absent
    #  3. Insérer le document avec livres.insert_one(...)
    #  4. Renvoyer {"insertedId": "<id sous forme de texte>"} avec le code 201
    #return jsonify({"erreur": "à implémenter"}), 501


# ---------- UPDATE ----------
@app.route("/api/livres/<id>", methods=["PUT"])
def modifier_livre(id):
    oid = vers_object_id(id)
    if oid is None:
        return jsonify({"erreur": "identifiant invalide"}), 400
    donnees = request.get_json(silent=True) or {}

    donnees.pop("_id", None)

    resultat = livres.update_one({"_id": oid}, {"$set": donnees})

    return jsonify({
        "matchedCount": resultat.matched_count,
        "modifiedCount": resultat.modified_count
    })
    # TODO Q3.4 :
    #  1. Retirer "_id" des données reçues (on ne modifie jamais l'identifiant)
    #  2. Mettre à jour avec livres.update_one({"_id": oid}, {"$set": donnees})
    #  3. Renvoyer {"matchedCount": ..., "modifiedCount": ...}
    return jsonify({"erreur": "à implémenter"}), 501


# ---------- DELETE ----------
@app.route("/api/livres/<id>", methods=["DELETE"])
def supprimer_livre(id):
    oid = vers_object_id(id)
    if oid is None:
        return jsonify({"erreur": "identifiant invalide"}), 400

    resultat = livres.delete_one({"_id": oid})

    if resultat.deleted_count == 0:
        return jsonify({"erreur": "livre introuvable"}), 404

    return jsonify({"deletedCount": resultat.deleted_count})
    # TODO Q3.5 :
    #  1. Supprimer avec livres.delete_one({"_id": oid})
    #  2. Si deleted_count vaut 0 -> {"erreur": "livre introuvable"} avec le code 404
    #  3. Sinon renvoyer {"deletedCount": 1}
    return jsonify({"erreur": "à implémenter"}), 501


if __name__ == "__main__":
    app.run(debug=True)
