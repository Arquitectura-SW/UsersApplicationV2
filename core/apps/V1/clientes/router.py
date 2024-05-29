from fastapi import APIRouter, Query
from .schemas import ClienteCreateSchema, ClienteUpdateSchema
from core.apps.V1.clientes import controller
router=APIRouter()


@router.get("/")
def get_all():
    return controller.get_all()

@router.get("/{document}")
def get_cliente(document: str):
    return controller.get_by_document(document)

@router.post("/")
async def create_cliente(cliente: ClienteCreateSchema):
    return controller.create(cliente)

@router.put("/{document}")
def update_cliente(document: str, cliente: ClienteUpdateSchema):
    return controller.update(document, cliente)

@router.delete("/{document}")
def delete_cliente(document: str):
    return controller.delete(document)