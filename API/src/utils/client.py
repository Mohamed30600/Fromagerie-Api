### CRUD Client
def create_client(db, client):
    db_client = db.Client(
        genrecli=client.genrecli,
        nomcli=client.nomcli,
        prenomcli=client.prenomcli,
        adresse1cli=client.adresse1cli,
        adresse2cli=client.adresse2cli,
        adresse3cli=client.adresse3cli,
        telcli=client.telcli,
        emailcli=client.emailcli,
        portcli=client.portcli,
        newsletter=client.newsletter,
        commune=db.Commune[client.commune.idcommune]
    )
    
    db.commit()
    return db_client

def update_client(db, id, client):
    db_client = db.Client[id]
    
    db_client.genrecli=client.genrecli
    db_client.nomcli=client.nomcli
    db_client.prenomcli=client.prenomcli
    db_client.adresse1cli=client.adresse1cli
    db_client.adresse2cli=client.adresse2cli
    db_client.adresse3cli=client.adresse3cli
    db_client.telcli=client.telcli
    db_client.emailcli=client.emailcli
    db_client.portcli=client.portcli
    db_client.newsletter=client.newsletter
    db_client.commune=db.Commune[client.commune.idcommune]
    
    db.commit()
    return db_client
    
def delete_client(db, id):
    db.Client[id].delete()
    db.commit()

def read_client(db, id):
    return db.Client[id]

def read_all_clients(db):
    return [c for c in db.Client.select()]
