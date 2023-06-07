from fastapi import APIRouter, HTTPException

routes=APIRouter()

@routes.get("/productos", status_code=200)
async def productos():   
        return "Esto es rutaProductos"
    