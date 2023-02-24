from pydantic import *
from datetime import datetime
from typing import Set, List

class CommuneInDB(BaseModel):
    idcommune : int
    departement : str
    codepostal : str
    ville : str
    class Config:
        orm_mode = True
    
class ClientInDB(BaseModel):
    codcli : int
    genrecli : str
    nomcli : str
    prenomcli : str
    adresse1cli : str
    adresse2cli : str
    adresse3cli : str
    telcli : str
    emailcli : str
    portcli : str
    newsletter : bool
    commune : CommuneInDB

    class Config:
        orm_mode = True
        
class Entete_CommandeInDB(BaseModel):
    codcde : int
    datcde : datetime
    timbrecli : int
    timbrecde : int
    nbcolis : int
    cheqcli : int
    idcondit : int
    cdeComt : str
    barchive : bool
    bstock : bool
    client : ClientInDB
    
    class Config:
        orm_mode = True
        
class Details_commandeInDB(BaseModel):
    idcommmande : int
    qtecommande : int
    datecreation : datetime
    entete_commande : Entete_CommandeInDB
    
    class Config:
        orm_mode = True
    
class ConditionnementInDB(BaseModel):
    idcondit = int
    libcondit = str
    prixcondit = float
    ordreimp = int
        
class ObjetInDB(BaseModel):
    codobj : int
    libobj : str
    tailleobj : str
    puobj : str
    poidsobj : str
    indisobj : str
    c_imp : int
    c_af1 : int
    c_cartp : bool
    points : int
    c_ordre_aff : int
    qt_debut : int
    qt_fin : int
    conditionnement = ConditionnementInDB
    
    class Config:
        orm_mode = True        
        
class PoidsVInDB(BaseModel):
    valmin : int
    valtimbre : int

    class Config:
        orm_mode = True  

class PoidsInDB(BaseModel):
    valmin : int
    valtimbre : int

    class Config:
        orm_mode = True  

class RoleInDB(BaseModel):
    coderole : int
    librole : str

    class Config:
        orm_mode = True  
    
    
class UtilisateurInDB(BaseModel):
    codeutilisateur : int
    nomutilisateur : str
    couleurfondutilisateur : str
    datecdeutilisateur : str
    roles : List[RoleInDB]
    
    @validator('roles', pre=True, allow_reuse=True)
    def pony_set_to_list(cls, values):
        return [v for v in values]

    class Config:
        orm_mode = True  



