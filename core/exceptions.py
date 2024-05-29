
from fastapi.responses import JSONResponse
from fastapi import Request, status
from fastapi.exceptions import HTTPException

class ClienteDoesNotExist(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_404_NOT_FOUND
        self.message = "Cliente does not exist"
    def __str__(self):
        return self.message
        
async def ClienteDoesNotExistHandler(request: Request, exc: ClienteDoesNotExist):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

class ClienteAlreadyExists(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_409_CONFLICT
        self.message = "Cliente already exists"
    def __str__(self):
        return self.message
    
async def ClienteAlreadyExistsHandler(request: Request, exc: ClienteAlreadyExists):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

class EmailAlreadyExists(HTTPException):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_409_CONFLICT
        self.message = "Email is already in use"
    def __str__(self):
        return self.message
    
async def EmailAlreadyExistsHandler(request: Request, exc: EmailAlreadyExists):
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})
    
