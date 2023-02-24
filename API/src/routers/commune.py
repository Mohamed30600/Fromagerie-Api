from fastapi import APIRouter, status, HTTPException

from typing import List
from src.schemas import CommuneInDB
from src.models import db
import src.utils.commune as utils

from pony.orm import db_session

#Gestionnaire de route fastAPI
router = APIRouter()

#Méthode de l'API pour créer une commune
@db_session
@router.post("/commune", response_model=CommuneInDB, status_code=status.HTTP_201_CREATED, tags=["Communes"])
async def create_commune(commune : CommuneInDB):
    db_commune = utils.create_commune(db,commune)
    return CommuneInDB.from_orm(db_commune)

#Méthode de l'API pour mettre à jour une commune via son id
@db_session
@router.put("/commune/{id}", response_model=CommuneInDB, tags=["Communes"])
async def update_commune(id: int, commune : CommuneInDB):
    db_commune = utils.update_commune(db,id,commune)
    return CommuneInDB.from_orm(db_commune)

#Méthode de l'API pour supprimer une commune via son id
@db_session
@router.delete("/commune/{id}", tags=["Communes"])
async def delete_commune(id: int):
    utils.delete_commune(db,id)
    return "suppression de la commune " + id

#Méthode de l'API pour récupérer une commune via son id
@db_session
@router.get("/commune/{id}", response_model=CommuneInDB, tags=["Communes"])
async def read_commune(id: int):
    db_commune = utils.read_commune(db,id)
    if db_commune is None:
        raise HTTPException(status_code=404, detail="Commune not found")
    return CommuneInDB.from_orm(db_commune)

#Méthode de l'API pour récupérer toutes les communes
@db_session
@router.get("/commune", response_model=List[CommuneInDB], tags=["Communes"])
async def read_all_commune():
    db_commune = utils.read_all_communes(db)
    return [CommuneInDB.from_orm(c) for c in db_commune]
