from .schemas import ClienteCreateSchema, ClienteUpdateSchema
from core.apps.V1.clientes import services
from fastapi.responses import JSONResponse


def create(cliente: ClienteCreateSchema) -> JSONResponse:
    data=services.create(cliente)
    return JSONResponse(status_code=201, content=data.model_dump())

def get_by_document(document: int) -> JSONResponse:
    data=services.get_by_document(document)
    return JSONResponse(status_code=200, content=data.model_dump())

def get_all() -> JSONResponse:
    data=services.get_all()
    return JSONResponse(status_code=200, content={
        "data": [cliente.model_dump() for cliente in data]
    })
    
def update(id: int, cliente: ClienteUpdateSchema) -> JSONResponse:
    data=services.update(id, cliente)
    return JSONResponse(status_code=200, content=data.model_dump())
    
def delete(document: int) -> JSONResponse:
    services.delete(document)
    return JSONResponse(status_code=200, content={
        "message": "Cliente deleted successfully"
    })