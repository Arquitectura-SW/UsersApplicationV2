from pydantic import BaseModel

class Cliente(BaseModel):
    name: str
    lastName: str
    document: int
    birthdate: str
    email: str
    country: str
    city: str
    income: float
    debt: float
    economicActivity: str
    company: str
    profession: str

    class Settings:
        collection = "clientes"