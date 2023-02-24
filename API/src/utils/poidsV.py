### CRUD pVColis
def create_pVColis(db,pvcolis):
    db_pVColis = db.PoidsV(
        valmin = pvcolis.valmin,
        valtimbre = pvcolis.valtimbre
    )
    db.commit()
    return db_pVColis

def update_pVColis(db, val, pvcolis):
    db_pVColis = db.PoidsV[val]
    
    db_pVColis.valmin = pvcolis.valmin
    db_pVColis.valtimbre = pvcolis.valtimbre
    
    db.commit()
    return db_pVColis

def delete_pVColis(db, val):
    db.PoidsV[val].delete()
    db.commit()
    
def read_pVColis(db, val):
    return db.PoidsV[val]
    
def read_all_pVColis(db):
    return [pc for pc in db.PoidsV.select()]
