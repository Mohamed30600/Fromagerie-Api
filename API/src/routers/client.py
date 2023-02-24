from fastapi import APIRouter, status, HTTPException, Depends

from typing import List
from src.schemas import ClientInDB, RoleInDB
from src.models import db
import src.utils.client as utils
#from src.utils import authprovider

from pony.orm import db_session

#PROTECTED = Depends(authprovider.HTTPHeaderAuthentication(db, scopes=[1]))
#, dependencies=[]

#Gestionnaire de route fastAPI
router = APIRouter()

#Méthode de l'API pour créer un client
@db_session
@router.post("/client", response_model=ClientInDB, status_code=status.HTTP_201_CREATED, tags=["Clients"])
async def create_client(client : ClientInDB):
    db_client = utils.create_client(db,client)
    return ClientInDB.from_orm(db_client)

#Méthode de l'API pour mettre à jour un client via son id
@db_session
@router.put("/client/{id}", response_model=ClientInDB, tags=["Clients"])
async def update_client(id : int, client : ClientInDB):
   db_client = utils.update_client(db,id,client)
   return ClientInDB.from_orm(db_client)

#Méthode de l'API pour supprimer un client via son id
@db_session
@router.delete("/client/{id}", tags=["Clients"])
async def delete_client(id: int):
    utils.delete_client(db,id)
    return "suppression du client id " + id

#Méthode de l'API pour récupérer un client via son id
@db_session
@router.get("/client/{id}", response_model=ClientInDB, tags=["Clients"])
async def read_client(id: int):
    db_client = utils.read_client(db,id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return ClientInDB.from_orm(db_client)

#Méthode de l'API pour récupérer tout les clients
@db_session
@router.get("/clients", response_model=List[ClientInDB], tags=["Clients"])
async def read_all_clients():
    db_clients = utils.read_all_clients(db)
    return [ClientInDB.from_orm(c) for c in db_clients]