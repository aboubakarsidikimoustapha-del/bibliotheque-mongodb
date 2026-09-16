"""Petit script de test de l'API avec le module requests (vu en cours)."""
import sys
import requests

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5000"

print("Santé :", requests.get(f"{BASE}/api/sante").json())

r = requests.post(f"{BASE}/api/livres", json={"titre": "Livre de test", "auteur": "Moi", "annee": 2026, "genre": "Test"})
print("POST :", r.status_code, r.json())
id_livre = r.json()["insertedId"]

print("GET  :", requests.get(f"{BASE}/api/livres/{id_livre}").json())
print("PUT  :", requests.put(f"{BASE}/api/livres/{id_livre}", json={"disponible": False}).json())
print("GET  :", requests.get(f"{BASE}/api/livres/{id_livre}").json())
print("DEL  :", requests.delete(f"{BASE}/api/livres/{id_livre}").json())
print("GET après suppression :", requests.get(f"{BASE}/api/livres/{id_livre}").status_code)
