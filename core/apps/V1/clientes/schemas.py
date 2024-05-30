from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
import re
import datetime

class ClienteCreateSchema(BaseModel):
    name: str = Field(..., max_length=150)
    lastName: str = Field(..., max_length=150)
    document: int = Field(..., ge=99999, le=999999999999999)
    birthdate: str = Field(...)
    email: EmailStr = Field(...)
    country: str = Field(..., max_length=50)
    city: str = Field(..., max_length=50)
    income: float = Field(..., gt=0)
    debt: float = Field(..., ge=0)
    economicActivity: str = Field(..., max_length=150)
    company: Optional[str] = Field(None, max_length=100)
    profession: Optional[str] = Field(None, max_length=150)

    class Config:
        schema_extra = {
            "example": {
                "name": "John",
                "lastName": "Doe",
                "document": "12345678",
                "birthdate": "1990-01-01",
                "email": "john.doe@example.com",
                "country": "USA",
                "city": "New York",
                "income": 50000.00,
                "debt": 10000.00,
                "economicActivity": "Software Development",
                "company": "Tech Solutions",
                "profession": "Software Engineer"
            }
        }
        
    @field_validator('birthdate')
    def validate_birthdate(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError('birthdate must be in the format YYYY-MM-DD')
        return v

    @field_validator('name', 'lastName', 'country', 'city', 'economicActivity', 'company', 'profession')
    def strip_and_sanitize(cls, v):
        # Strip whitespace
        v = v.strip()
        # Remove any characters that could be used for injection
        v = re.sub(r'[^\w\s-]', '', v)
        return v


class ClienteSchema(ClienteCreateSchema):
    _id: str
    name: str = Field(..., max_length=150)
    lastName: str = Field(..., max_length=150)
    birthdate: str = Field(...)
    document: int = Field(..., ge=99999, le=999999999999999)
    email: EmailStr = Field(...)
    country: str = Field(..., max_length=50)
    city: str = Field(..., max_length=50)
    income: float = Field(..., gt=0)
    debt: float = Field(..., ge=0)
    economicActivity: str = Field(..., max_length=150)
    company: Optional[str] = Field(None, max_length=100)
    profession: Optional[str] = Field(None, max_length=150)
    

class ClienteUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=150)
    lastName: Optional[str] = Field(None, max_length=150)
    birthdate: Optional[str] = Field(None)
    country: Optional[str] = Field(None, max_length=50)
    city: Optional[str] = Field(None, max_length=50)
    income: Optional[float] = Field(None, gt=0)
    debt: Optional[float] = Field(None, ge=0)
    economicActivity: Optional[str] = Field(None, max_length=150)
    company: Optional[str] = Field(None, max_length=100)
    profession: Optional[str] = Field(None, max_length=150)
    