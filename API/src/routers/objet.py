from fastapi import APIRouter, status, HTTPException

from typing import List
from src.schemas import ObjetInDB
from src.models import db
import src.utils.objet as utils

from pony.orm import db_session

#Gestionnaire de route fastAPI
router = APIRouter()

#Méthode de l'API pour créer un objet
@db_session
@router.post("/objet", response_model=ObjetInDB, status_code=status.HTTP_201_CREATED, tags=["Objets"])
async def create_objet(objet : ObjetInDB):
    db_objet = utils.create_objet(db,objet)
    return ObjetInDB.from_orm(db_objet)

#Méthode de l'API pour mettre à jour un objet via son id
@db_session
@router.put("/objet/{id}", response_model=ObjetInDB, tags=["Objets"])
async def update_objet(id: int, objet : ObjetInDB):
    db_objet = utils.update_objet(db,id,objet)
    return ObjetInDB.from_orm(db_objet)

#Méthode de l'API pour supprimer un objet via son id
@db_session
@router.delete("/objet/{id}", tags=["Objets"])
async def delete_objet(id: int):
    utils.delete_objet(db,id)
    return "suppression de l'objet id " + id

#Méthode de l'API pour récupérer un utilisateur via son id
@db_session
@router.get("/objet/{id}", response_model=ObjetInDB, tags=["Objets"])
async def read_objet(id: int):
    db_objet = utils.read_objet(db,id)
    if db_objet is None:
        raise HTTPException(status_code=404, detail="Objet not found")
    return ObjetInDB.from_orm(db_objet)


#Méthode de l'API pour récupérer tout les objets
@db_session
@router.get("/objets", response_model=List[ObjetInDB], tags=["Objets"])
async def read_all_objets():
    db_objets = utils.read_all_objets(db)
    return [ObjetInDB.from_orm(c) for c in db_objets]