from fastapi import APIRouter, status, HTTPException

from typing import List
from src.schemas import PoidsVInDB
from src.models import db
import src.utils.poidsV as utils
from pony.orm import db_session

#Gestionnaire de route fastAPI
router = APIRouter()

#Méthode de l'API pour créer un poids vignette colis
@db_session
@router.post("/pVcolis", response_model=PoidsVInDB, status_code=status.HTTP_201_CREATED, tags=["Poids Vignette Colis"])
async def create_pVColis(pColis : PoidsVInDB):
    db_pVColis = utils.create_pVColis(db,pColis)
    return PoidsVInDB.from_orm(db_pVColis)

#Méthode de l'API pour mettre à jour un poids vignette colis 
@db_session
@router.put("/pVcolis/{val}", response_model=PoidsVInDB, tags=["Poids Vignette Colis"])
async def update_pVColis(val: int, pVColis : PoidsVInDB):
    db_pVColis = utils.update_pVColis(db,val,pVColis)
    return PoidsVInDB.from_orm(db_pVColis)

#Méthode de l'API pour supprimer un poids vignette colis
@router.delete("/pVcolis/{val}", tags=["Poids Vignette Colis"])
async def delete_pVColis(val: int):
    utils.delete_pVColis(db,val)
    return "suppression du poids vignette de valeur " + val


#Méthode de l'API pour récupérer un poids vignette colis
@db_session
@router.get("/pVcolis/{val}", response_model=PoidsVInDB, tags=["Poids Vignette Colis"])
async def read_pVColis(val: int):
    db_pVColis = utils.read_pVColis(db,val)
    if db_pVColis is None:
        raise HTTPException(status_code=404, detail="Poids Vignette not found")
    return PoidsVInDB.from_orm(db_pVColis)

#Méthode de l'API pour récupérer tout les poids vignette colis
@db_session
@router.get("/pVcolis", response_model=List[PoidsVInDB], tags=["Poids Vignette Colis"])
async def read_all_pVColis():
    db_pVColis = utils.read_all_pVColis(db)
    return [PoidsVInDB.from_orm(c) for c in db_pVColis]