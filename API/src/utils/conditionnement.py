### CRUD Conditionnement
def create_conditionnement(db, conditionnement):

    db_conditionnement = db.Conditionnement(
        libcondit = conditionnement.libcondit,
        prixcondit = conditionnement.prixcondit,
        ordreimp = conditionnement.ordreimp
    )

    db.commit()
    return db_conditionnement

def update_conditionnement(db, id, conditionnement):
    db_conditionnement = db.Conditionnement[id]
    
    db_conditionnement.idcondit = conditionnement.idcondit
    db_conditionnement.libcondit = conditionnement.libcondit
    db_conditionnement.prixcondit = conditionnement.prixcondit
    db_conditionnement.ordreimp = conditionnement.ordreimp
    
    db.commit()
    return db_conditionnement
    
def delete_conditionnement(db, id):
    db.Conditionnement[id].delete()
    db.commit()

def read_conditionnement(db, id):
    return db.Conditionnement[id]

def read_all_conditionnements(db):
    return [c for c in db.Conditionnement.select()]
