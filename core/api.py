from fastapi import APIRouter
from core.apps.V1.clientes.router import router as clientes_router

router=APIRouter()

router.include_router(clientes_router, prefix="/v1/clientes", tags=["Clientes"])