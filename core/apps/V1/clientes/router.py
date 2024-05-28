from fastapi import APIRouter

router=APIRouter()

@router.get("/")
def get_all_clientes():
    return {"message": "Get all clientes"}

@router.get("/{id}")
def get_cliente(id: int):
    return {"message": f"Get cliente {id}"}

@router.post("/")
def create_cliente():
    return {"message": "Create cliente"}

@router.put("/{id}")
def update_cliente(id: int):
    return {"message": f"Update cliente {id}"}

@router.delete("/{id}")
def delete_cliente(id: int):
    return {"message": f"Delete cliente {id}"}