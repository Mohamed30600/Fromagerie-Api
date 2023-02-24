from fastapi import APIRouter, status, HTTPException

from typing import List
from src.schemas import ConditionnementInDB
from src.models import db
import src.utils.conditionnement as utils

from pony.orm import db_session

#Gestionnaire de route fastAPI
router = APIRouter()

#Méthode de l'API pour créer un conditionnement
@db_session
@router.post("/conditionnement", response_model=ConditionnementInDB, status_code=status.HTTP_201_CREATED, tags=["Conditionnements"])
async def create_conditionnement(conditionnement : ConditionnementInDB):
    db_conditionnement = utils.create_conditionnement(db,conditionnement)
    return ConditionnementInDB.from_orm(db_conditionnement)

#Méthode de l'API pour mettre à jour un conditionnement via son id
@router.put("/conditionnement/{id}", response_model=ConditionnementInDB, tags=["Conditionnements"])
def update_conditionnement(id: int, conditionnement : ConditionnementInDB):
    db_conditionnement = utils.update_conditionnement(db,id,conditionnement)
    return ConditionnementInDB.from_orm(db_conditionnement)

#Méthode de l'API pour supprimer un conditionnement via son id
@router.delete("/conditionnement/{id}", tags=["Conditionnements"])
def delete_conditionnement(id: int):
    utils.delete_conditionnement(db,id)
    return "suppression du conditionnement id " + id

#Méthode de l'API pour récupérer un conditionnement via son id
@db_session
@router.get("/conditionnement/{id}", response_model=ConditionnementInDB, tags=["Conditionnements"])
async def read_conditionnement(id: int):
    db_conditionnement = utils.read_conditionnement(db,id)
    if db_conditionnement is None:
        raise HTTPException(status_code=404, detail="Conditionnement not found")
    return ConditionnementInDB.from_orm(db_conditionnement)

#Méthode de l'API pour récupérer tout les conditionnements
@db_session
@router.get("/conditionnements", response_model=List[ConditionnementInDB], tags=["Conditionnements"])
async def read_all_conditionnement():
    db_conditionnements = utils.read_all_conditionnements(db)
    return [ConditionnementInDB.from_orm(c) for c in db_conditionnements]