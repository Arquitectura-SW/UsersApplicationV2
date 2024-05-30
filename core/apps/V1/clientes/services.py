from ....mongodb import clientes
from .schemas import ClienteCreateSchema, ClienteSchema, ClienteUpdateSchema
from core.exceptions import ClienteDoesNotExist, ClienteAlreadyExists, EmailAlreadyExists
from core.logs.producer import log

def create(cliente : ClienteCreateSchema) -> ClienteSchema:
    if exists(cliente.document):
        raise ClienteAlreadyExists()
    if email_exists(cliente.email):
        raise EmailAlreadyExists()
    result = clientes.insert_one(cliente.model_dump())
    log(document=cliente.document, level="INFO", message="Cliente creado exitosamente") 
    data= ClienteSchema(
        _id=str(result.inserted_id),
        name=cliente.name,
        lastName=cliente.lastName,
        document=cliente.document,
        birthdate=cliente.birthdate,
        email=cliente.email,
        country=cliente.country,
        city=cliente.city,
        income=cliente.income,
        debt=cliente.debt,
        economicActivity=cliente.economicActivity,
        company=cliente.company,
        profession=cliente.profession
    )
    return data

def get_by_document(document: int) -> ClienteSchema:
    data = clientes.find_one({"document": str(document)})
    if not data:
        print("No existe el cliente")
        print(data)
        raise ClienteDoesNotExist()
    log(document=document, level="INFO", message="Se retorno la informacion del cliente")
    return ClienteSchema(
        _id=str(data.get('_id')),
        name=data.get('name'),
        lastName=data.get('lastName'),
        document=data.get('document'),
        birthdate=data.get('birthdate'),
        email=data.get('email'),
        country=data.get('country'),
        city=data.get('city'),
        income=data.get('income'),
        debt=data.get('debt'),
        economicActivity=data.get('economicActivity'),
        company=data.get('company'),
        profession=data.get('profession')
    )
    
def get_by_email(email: str) -> ClienteSchema:
    data = clientes.find_one({"email": email})
    if not data:
        raise EmailAlreadyExists()
    log(email=email, level="INFO", message="Se retorno la informacion del cliente")
    return ClienteSchema(
        _id=str(data.get('_id')),
        name=data.get('name'),
        lastName=data.get('lastName'),
        document=data.get('document'),
        birthdate=data.get('birthdate'),
        email=data.get('email'),
        country=data.get('country'),
        city=data.get('city'),
        income=data.get('income'),
        debt=data.get('debt'),
        economicActivity=data.get('economicActivity'),
        company=data.get('company'),
        profession=data.get('profession')
    )

def exists(document: int) -> bool:
    data= clientes.find_one({"document": str(document)})
    if data:
        return True
    return False

def email_exists(email: str) -> bool:
    data= clientes.find_one({"email": email})
    if data:
        return True
    return False

def get_all():
    data = clientes.find()
    return [ClienteSchema(
        _id=str(item.get('_id')),
        name=item.get('name'),
        lastName=item.get('lastName'),
        document=item.get('document'),
        birthdate=item.get('birthdate'),
        email=item.get('email'),
        country=item.get('country'),
        city=item.get('city'),
        income=item.get('income'),
        debt=item.get('debt'),
        economicActivity=item.get('economicActivity'),
        company=item.get('company'),
        profession=item.get('profession')
    ) for item in data]

def delete(document: int) -> bool:
    if not exists(document):
        print("entro")
        raise ClienteDoesNotExist()
    if clientes.delete_one({"document": str(document)})
        log(document=document, level="INFO", message="Cliente eliminado exitosamente")
        return True
    return False

def update(document: int, client: ClienteUpdateSchema) -> ClienteSchema:
    if not exists(document):
        raise ClienteDoesNotExist()
    data= clientes.find_one_and_update({"document": str(document)}, {"$set": client.model_dump()}, return_document=True)
    log(document=document, level="INFO", message="Cliente actualizado exitosamente")
    return ClienteSchema(
        _id=str(data.get('_id')),
        name=data.get('name'),
        lastName=data.get('lastName'),
        document=data.get('document'),
        birthdate=data.get('birthdate'),
        email=data.get('email'),
        country=data.get('country'),
        city=data.get('city'),
        income=data.get('income'),
        debt=data.get('debt'),
        economicActivity=data.get('economicActivity'),
        company=data.get('company'),
        profession=data.get('profession')
    )