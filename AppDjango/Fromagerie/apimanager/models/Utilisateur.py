from .Role import Role

class Utilisateur:
    def __init__(self, codeutilisateur, nomutilisateur, couleurfondutilisateur, datecdeutilisateur, login, pwd, **roles):
        self.codeutilisateur = codeutilisateur
        self.nomutilisateur = nomutilisateur
        self.couleurfondutilisateur = couleurfondutilisateur
        self.datecdeutilisateur = datecdeutilisateur
        self.login = login
        self.pwd = pwd
        self.roles = [Role(**r) for r in roles['roles']]
        
    def isAdmin(self):
        for role in self.roles:
            if role.librole == "Administrateur":
                return True
        
        return False