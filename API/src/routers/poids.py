from fastapi import APIRouter, status, HTTPException

from typing import List
from src.schemas import PoidsInDB
from src.models import db
import src.utils.poids as utils
from pony.orm import db_session

#Gestionnaire de route fastAPI
router = APIRouter()

#Méthode de l'API pour créer un poids colis
@db_session
@router.post("/pcolis", response_model=PoidsInDB, status_code=status.HTTP_201_CREATED, tags=["Poids Colis"])
async def create_pColis(pColis : PoidsInDB):
    db_pColis = utils.create_pColis(db,pColis)
    return PoidsInDB.from_orm(db_pColis)

#Méthode de l'API pour mettre à jour un poids colis 
@db_session
@router.put("/pcolis/{val}", response_model=PoidsInDB, tags=["Poids Colis"])
async def update_pColis(val: int, pColis : PoidsInDB):
    db_pColis = utils.update_pColis(db,val,pColis)
    return PoidsInDB.from_orm(db_pColis)

#Méthode de l'API pour supprimer un poids colis
@db_session
@router.delete("/pcolis/{val}", tags=["Poids Colis"])
async def delete_pColis(val: int):
    utils.delete_pColis(db,val)
    return "suppression du poids de valeur " + val

#Méthode de l'API pour récupérer un poids colis
@db_session
@router.get("/pcolis/{val}", response_model=PoidsInDB, tags=["Poids Colis"])
async def read_pColis(val: int):
    db_pColis = utils.read_pColis(db,val)
    if db_pColis is None:
        raise HTTPException(status_code=404, detail="Poids not found")
    return PoidsInDB.from_orm(db_pColis)

#Méthode de l'API pour récupérer tout les poids colis
@db_session
@router.get("/pcolis", response_model=List[PoidsInDB], tags=["Poids Colis"])
async def read_all_pColis():
    db_pColis = utils.read_all_pColis(db)
    return [PoidsInDB.from_orm(c) for c in db_pColis]
