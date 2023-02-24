### CRUD Utilisateur
def create_utilisateur(db, utilisateur):

    db_utilisateur = db.Utilisateur(
        nomutilisateur = utilisateur.nomutilisateur,
        couleurfondutilisateur = utilisateur.couleurfondutilisateur,
        datecdeutilisateur = utilisateur.datecdeutilisateur,
        login = utilisateur.login,
        pwd = utilisateur.pwd,
        roles = [db.Role[r.coderole] for r in utilisateur.roles]
        )
    db.commit()
    return db_utilisateur

def update_utilisateur(db, id, utilisateur):
    db_utilisateur = db.Utilisateur[id]
    
    db_utilisateur.nomutilisateur = utilisateur.nomutilisateur
    db_utilisateur.couleurfondutilisateur = utilisateur.couleurfondutilisateur
    db_utilisateur.datecdeutilisateur = utilisateur.datecdeutilisateur
    db_utilisateur.login = utilisateur.login
    db_utilisateur.pwd = utilisateur.pwd
    db_utilisateur.roles = [db.Role[r.coderole] for r in utilisateur.roles]
    
    db.commit()
    return db_utilisateur
    
def delete_utilisateur(db, id):
    db.Utilisateur[id].delete()
    db.commit()

def read_utilisateur(db, id):
    return db.Utilisateur[id]

def read_all_utilisateurs(db):
    return [u for u in db.Utilisateur.select()]

def get_utilisateur_from_login(db, login, password):
    return db.Utilisateur.select(lambda u: u.login == login and u.pwd == password)
