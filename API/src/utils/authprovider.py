from fastapi import Header
from typing import Set, List
from starlette.requests import Request
from starlette.exceptions import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from src.models import Utilisateur
from src.schemas import UtilisateurInDB, RoleInDB

class HTTPHeaderAuthentication:
    def __init__(self, db, scopes: List[int]):
        self.scopes = scopes
        self.db = db

    async def __call__(self, request: Request, authuser: str = Header(None)) -> UtilisateurInDB:
        user = self.locate_user(username=authuser)
        if not user:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
            )
        if not self.has_required_scope(user.roles):
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED, detail=f"{user.nomutilisateur} is not authorized to access this endpoint"
            )
        return user

    def locate_user(self, username: str) -> UtilisateurInDB:
        """Mock lookup in repository"""
        user = self.db.Utilisateur.select(lambda u: u.nomutilisateur == username)
        
        return UtilisateurInDB.from_orm(user)

    def has_required_scope(self, user_scopes: List[RoleInDB]) -> bool:
        """Verify the user has the desired auth scope"""
        scopes = [RoleInDB.from_orm(r) for r in self.db.Role.select()]
        print(scopes)
        for scope in scopes:
            if scope not in user_scopes:
                return False
        return True