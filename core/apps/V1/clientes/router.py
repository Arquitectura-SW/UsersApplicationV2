from fastapi import APIRouter
from .schemas import ClienteCreateSchema, ClienteUpdateSchema
from core.apps.V1.clientes import controller
router=APIRouter()


@router.get("/clientes/")
def get_all():
    return controller.get_all()

@router.get("/cliente/{document}")
def get_cliente(document: int):
    return controller.get_by_document(document)

@router.post("/createCliente/")
async def create_cliente(cliente: ClienteCreateSchema):
    return controller.create(cliente)

@router.put("/updateCliente/{document}")
def update_cliente(document: int, cliente: ClienteUpdateSchema):
    return controller.update(document, cliente)

@router.delete("/clienteDelete/{document}")
def delete_cliente(document: int):
    return controller.delete(document)