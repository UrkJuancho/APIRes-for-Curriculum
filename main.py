from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title="API para Hojas de Vida",
    description="API Creada para gestionar los datos tipicos de una hoja de vida o curriculum para luego implementarlos en un proyecto al consumirlos",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(user)
