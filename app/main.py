from fastapi import FastAPI
from .routers import assembly
app = FastAPI()
app.include_router(assembly.router, prefix="/assemblies")
