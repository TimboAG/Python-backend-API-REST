from fastapi import APIRouter, HTTPException

routes=APIRouter()

@routes.post("/login", status_code=200)
async def login():   
        return "Esto es rutaProductos"