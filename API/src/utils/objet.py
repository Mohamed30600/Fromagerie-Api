### CRUD Objet
def create_objet(db, objet):
    
    db_objet = db.Objet(
        libobj = objet.libobj,
        tailleobj = objet.tailleobj,
        puobj = objet.puobj,
        poidsobj = objet.poidsobj,
        indisobj = objet.indisobj,
        c_imp = objet.c_imp,
        c_af1 = objet.c_af1,
        c_cartp = objet.c_cartp,
        points = objet.points,
        c_ordre_aff = objet.c_ordre_aff,
        qt_debut = objet.qt_debut,
        qt_fin = objet.qt_fin,
        conditionnement = db.Conditionnement[objet.conditionnement.idcondit]
    )
    
    db.commit()
    return db_objet

def update_objet(db, id, objet):
    db_objet = db.Objet[id]
    
    db_objet.libobj = objet.libobj
    db_objet.tailleobj = objet.tailleobj
    db_objet.puobj = objet.puobj
    db_objet.poidsobj = objet.poidsobj
    db_objet.indisobj = objet.indisobj
    db_objet.c_imp = objet.c_imp
    db_objet.c_af1 = objet.c_af1
    db_objet.c_cartp = objet.c_cartp
    db_objet.points = objet.points
    db_objet.c_ordre_aff = objet.c_ordre_aff
    db_objet.qt_debut = objet.qt_debut
    db_objet.qt_fin = objet.qt_fin
    db_objet.conditionnement = db.Conditionnement[objet.conditionnement.idcondit]
    
    db.commit()
    return db_objet

def delete_objet(db,id):
    db.Objet[id].delete()
    db.commit()

def read_objet(db,id):
    return db.Objet[id]

def read_all_objets(db):
    return [o for o in db.Objet.select()]
