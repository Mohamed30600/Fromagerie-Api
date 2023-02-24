### CRUD pColis
def create_pColis(db,pcolis):
    db_pColis = db.Poids(
        valmin = pcolis.valmin,
        valtimbre = pcolis.valtimbre
    )
    db.commit()
    return db_pColis

def update_pColis(db, val, pcolis):
    db_pColis = db.Poids[val]
    
    db_pColis.valmin = pcolis.valmin
    db_pColis.valtimbre = pcolis.valtimbre
    
    db.commit()
    return db_pColis

def delete_pColis(db, val):
    db.Poids[val].delete()
    db.commit()
    
def read_pColis(db, val):
    return db.Poids[val]
    
def read_all_pColis(db):
    return [pc for pc in db.Poids.select()]
