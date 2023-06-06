from fastapi import FastAPI
from pydantic import BaseModel
from funciones.funcionUsuario import *

app=FastAPI()

@app.get("/usuarios")
async def usuarios():
    return mostrar_usuarios()

#Por path
@app.get("/usuario/{id}")
async def usuario(id:int):
    return buscar_usuario_id(id)

#Por query
@app.get("/usuario/")
async def usuario(id:int):
    return buscar_usuario_id(id)
    
    