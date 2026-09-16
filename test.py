import requests 
r = requests.post("http://127.0.0.1:5000/api/livres", json={"titre": "Dune", "auteur": 
"Frank Herbert", "annee": 1965, "genre": "SF"}) 
print(r.status_code, r.json()) 