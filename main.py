import uvicorn

from fastapi import FastAPI
from core.config.config import HOST, PORT
from core.api import router as api
from core import exceptions
description = """
This is a simple Users Application for Banco Los Alpes.
"""
app = FastAPI(
    title="Users Application",
    version="1.0.0",
    description=description,
)

app.add_exception_handler(exceptions.ClienteDoesNotExist, exceptions.ClienteDoesNotExistHandler)
app.add_exception_handler(exceptions.ClienteAlreadyExists, exceptions.ClienteAlreadyExistsHandler)
app.add_exception_handler(exceptions.EmailAlreadyExists, exceptions.EmailAlreadyExistsHandler)

#default route
@app.get("/")
async def home():
    return {"message": "Server is running"}


app.include_router(api, prefix="/api")
if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)