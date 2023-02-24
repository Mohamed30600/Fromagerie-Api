### CRUD commune
def create_commune(db,commune):
    db_commune = db.Commune(
        departement=commune.departement,
        codepostal=commune.codepostal,
        ville=commune.ville
    )
    db.commit()
    return db_commune

def update_commune(db, id, commune):
    db_commune = db.Poids[id]
    
    db_commune.departement=commune.departement
    db_commune.codepostal=commune.codepostal
    db_commune.ville=commune.vill
    
    db.commit()
    return db_commune

def delete_commune(db, id):
    db.Commune[id].delete()
    db.commit()
    
def read_commune(db, id):
    return db.Commune[id]
    
def read_all_communes(db):
    return [c for c in db.Commune.select()]
