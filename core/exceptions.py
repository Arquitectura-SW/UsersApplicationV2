
from fastapi.responses import JSONResponse
from fastapi import Request, status
from fastapi.exceptions import HTTPException
from core.logs.producer import log

class ClienteDoesNotExist(HTTPException):
    document: int
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_404_NOT_FOUND
        self.message = "Cliente does not exist"
        self.document = kwargs.get('document')        
    def __str__(self):
        return self.message
        
async def ClienteDoesNotExistHandler(request: Request, exc: ClienteDoesNotExist):
    log(document=0, level="ERROR", message=exc.message)
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})

class ClienteAlreadyExists(HTTPException):
    document: int
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status.HTTP_409_CONFLICT
        self.message = "Cliente already exists"
        self.document = kwargs.get('document')
    def __str__(self):
        return self.message
    
async def ClienteAlreadyExistsHandler(request: Request, exc: ClienteAlreadyExists):
    log(document=0, level="ERROR", message=exc.message)
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
    log(document=0, level="ERROR", message=exc.message)
    return JSONResponse(status_code=exc.status_code, 
    content={"message": exc.message})
    
