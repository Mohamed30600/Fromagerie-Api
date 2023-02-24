from apimanager.models.Utilisateur import Utilisateur
from apimanager.models.Role import Role
import requests

#Fonction qui récupère une liste de tout les utilisateurs en appelant l'API. Renvoit une liste d'objet "Utilisateur"
def getUsers():
    response = requests.get("http://localhost:8000/utilisateurs")
    raw = response.json()
    return [Utilisateur(**user) for user in raw]

#Fonction qui récupère un utilisateur à partir d'un login et d'un password en appelant l'API. Renvoit un objet "Utlisateur" si les identifiants sont bons.
def getUserFromLogin(login, password):
    logs = { 'login':login, 'password':password }
    response = requests.post("http://localhost:8000/utilisateurFromLogin", json = logs)
    if response.status_code == 404 :
        return None
    else:
        raw = response.json()
        return [Utilisateur(**user)for user in raw][0]


