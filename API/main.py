from src.models import db
from src.config import Settings
from src.routers import client, conditionnement, objet, poids, poidsV, utilisateur, commune
from src.schemas import *

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Description pour Swagger
description = """
Fromagerie API. 🧀

* **CRUD** Client
* **CRUD** Commune
* **CRUD** Conditionnement
* **CRUD** Objet
* **CRUD** Poids Colis
* **CRUD** Poids Vignette Colis
* **CRUD** Poids Vignette Colis
* **CRUD** Utilisateur
* **Lecture d'un Utilisateur via ses logins**
* **Creation d'une commande**

"""
#Tags pour Swagger
tags_metadata = [
    {
        "name": "Clients",
        "description": "**Opérations sur les utilisateurs.** (Create, Delete, Update, ReadOne, ReadAll)"
    },
    {
        "name": "Communes",
        "description": "**Opérations sur les communes.** (Create, Delete, Update, ReadOne, ReadAll)"
    },
    {
        "name": "Conditionnements",
        "description": "**Opérations sur les conditionnements.** (Create, Delete, Update, ReadOne, ReadAll)"
    },
    {
        "name": "Objets",
        "description": "**Opérations sur les objets.** (Create, Delete, Update, ReadOne, ReadAll)"
    },
    {
        "name": "Poids Colis",
        "description": "**Opérations sur les poids colis.** (Create, Delete, Update, ReadOne, ReadAll)"
    },
    {
        "name": "Poids Vignette Colis",
        "description": "**Opérations sur les poids vignette colis.** (Create, Delete, Update, ReadOne, ReadAll)"
    },
    {
        "name": "Utilisateurs",
        "description": "**Opérations sur les utilisateurs.** (Create, Delete, Update, ReadOne, ReadAll, ReadOneFromLogin)"
    }
    
]

#Lecture du fichier .env et mis en forme via le schema Pydantic
settings = Settings(_env_file='.env', _env_file_encoding='utf-8')

#Connexion à la base de données
db.bind(provider=settings.provider, host=settings.host, user=settings.user, passwd=settings.passwd, db=settings.db)
#Génération du mapping via l'orm Pony
db.generate_mapping(create_tables=True)

app = FastAPI(
    title="Fromagerie API",
    description=description,
    version=1.0,
    openapi_tags=tags_metadata
)

#Gestion des crossorigins
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Inclusion des routers dans l'API fastAPI
app.include_router(client.router)
app.include_router(commune.router)
app.include_router(conditionnement.router)
app.include_router(objet.router)
app.include_router(poids.router)
app.include_router(poidsV.router)
app.include_router(utilisateur.router)