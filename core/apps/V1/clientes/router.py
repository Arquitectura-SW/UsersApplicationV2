from fastapi import APIRouter, Query
from .schemas import ClienteCreateSchema, ClienteUpdateSchema
from core.apps.V1.clientes import controller
router=APIRouter()


@router.get("/")
def get_all():
    return controller.get_all()

@router.get("/{document}")
def get_cliente(document: int = Query(..., ge=99999, le=999999999999999)):
    return controller.get_by_document(document)

@router.post("/")
async def create_cliente(cliente: ClienteCreateSchema):
    return controller.create(cliente)

@router.put("/{document}")
def update_cliente(document: int, cliente: ClienteUpdateSchema):
    return controller.update(document, cliente)

@router.delete("/{document}")
def delete_cliente(document: int):
    return controller.delete(document)