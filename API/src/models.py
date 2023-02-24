from datetime import datetime
from pony.orm import *


db = Database()


class Client(db.Entity):
    codcli = PrimaryKey(int, auto=True)
    genrecli = Optional(str)
    nomcli = Optional(str)
    prenomcli = Optional(str)
    adresse1cli = Optional(str)
    adresse2cli = Optional(str)
    adresse3cli = Optional(str)
    telcli = Optional(str)
    emailcli = Optional(str)
    portcli = Optional(str)
    newsletter = Optional(bool, default=True)
    commune = Required('Commune')
    entete__commandes = Set('Entete_Commande')


class Entete_Commande(db.Entity):
    codcde = PrimaryKey(int, auto=True)
    datcde = Optional(datetime)
    timbrecli = Optional(int)
    timbrecde = Optional(int)
    nbcolis = Optional(int)
    cheqcli = Optional(int)
    idcondit = Optional(int)
    cdeComt = Optional(str)
    barchive = Optional(bool, default=True)
    bstock = Optional(bool, default=True)
    client = Required(Client)
    details_commandes = Set('Details_commande')


class Commune(db.Entity):
    idcommune = PrimaryKey(int, auto=True)
    departement = Optional(str)
    codepostal = Optional(str)
    ville = Optional(str)
    clients = Set(Client)


class Details_commande(db.Entity):
    idcommmande = PrimaryKey(int, auto=True)
    qtecommande = Optional(int)
    datecreation = Optional(datetime)
    entete_commande = Required(Entete_Commande)
    objets = Set('Objet')


class Objet(db.Entity):
    codobj = PrimaryKey(int, auto=True)
    libobj = Optional(str)
    tailleobj = Optional(str)
    puobj = Optional(str)
    poidsobj = Optional(str)
    indisobj = Optional(str)
    c_imp = Optional(int)
    c_af1 = Optional(int)
    c_cartp = Optional(bool, default=True)
    points = Optional(int)
    c_ordre_aff = Optional(int)
    qt_debut = Optional(int)
    qt_fin = Optional(int)
    details_commandes = Set(Details_commande)
    conditionnement = Required('Conditionnement')


class Conditionnement(db.Entity):
    idcondit = PrimaryKey(int, auto=True)
    libcondit = Optional(str)
    prixcondit = Optional(float)
    ordreimp = Optional(int)
    objets = Set(Objet)


class PoidsV(db.Entity):
    valmin = Optional(int)
    valtimbre = Optional(int)


class Poids(db.Entity):
    valmin = Optional(int)
    valtimbre = Optional(int)


class Utilisateur(db.Entity):
    codeutilisateur = PrimaryKey(int, auto=True)
    nomutilisateur = Optional(str)
    couleurfondutilisateur = Optional(str)
    datecdeutilisateur = Optional(str)
    login = Optional(str)
    pwd = Optional(str)
    roles = Set('Role')


class Role(db.Entity):
    coderole = PrimaryKey(int, auto=True)
    librole = Optional(str)
    utilisateurs = Set(Utilisateur)

