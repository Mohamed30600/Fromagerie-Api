from fastapi import APIRouter, status, HTTPException

from typing import List
from src.schemas import UtilisateurInDB,RoleInDB, LoginSchema
from src.models import db
import src.utils.utilisateur as utils
from pony.orm import db_session

router = APIRouter()

@db_session
@router.post("/utilisateur", response_model=UtilisateurInDB, status_code=status.HTTP_201_CREATED, tags=["Utilisateurs"])
async def create_utilisateur(utilisateur : UtilisateurInDB):
    db_utilisateur = utils.create_utilisateur(db,utilisateur)
    return UtilisateurInDB.from_orm(db_utilisateur)

@db_session
@router.put("/utilisateur/{id}", response_model=UtilisateurInDB, tags=["Utilisateurs"])
async def update_utilisateur(id: int, utilisateur : UtilisateurInDB):
    db_utilisateur = utils.update_utilisateur(db,id,utilisateur)
    return UtilisateurInDB.from_orm(db_utilisateur)

@db_session
@router.delete("/utilisateur/{id}", tags=["Utilisateurs"])
async def delete_utilisateur(id: int):
    utils.delete_utilisateur(db,id)
    return "suppression du utilisateur id " + id

@db_session
@router.get("/utilisateur/{id}", response_model=UtilisateurInDB, tags=["Utilisateurs"])
async def read_utilisateur(id: int):
    db_utilisateur = utils.read_utilisateur(db,id)
    if db_utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return UtilisateurInDB.from_orm(db_utilisateur)

@db_session
@router.get("/utilisateurs", response_model=List[UtilisateurInDB], tags=["Utilisateurs"])
async def read_all_utilisateurs():
    db_utilisateur = utils.read_all_utilisateurs(db)
    return [UtilisateurInDB.from_orm(u) for u in db_utilisateur]

@db_session
@router.post("/utilisateurFromLogin", response_model=List[UtilisateurInDB], tags=["Utilisateurs"])
async def read_utilisateur_from_login(log : LoginSchema):
    db_utilisateur = utils.get_utilisateur_from_login(db, log.login, log.password)
    if len(db_utilisateur) == 0:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return [UtilisateurInDB.from_orm(u) for u in db_utilisateur]