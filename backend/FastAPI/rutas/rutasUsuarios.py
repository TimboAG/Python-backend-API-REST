from fastapi import APIRouter, HTTPException
from funciones.funcionUsuario import *

routes=APIRouter()

@routes.get("/usuarios", status_code=200)
async def usuarios():
    try:
        return mostrar_usuarios()
    except:
        raise HTTPException(status_code=404, detail="Ocurrio un error")

#Por path
@routes.get("/usuario/{id}", status_code=200)
async def usuario(id:int):
    try:
        return buscar_usuario_id(id)
    except:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    

#Por query
@routes.get("/usuario/", status_code=200)
async def usuario(id:int):
    try:
        return buscar_usuario_id(id)
    except:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")

@routes.post("/usuario/", status_code=201)
async def usuario(usuario: Usuario):   
    if type(buscar_usuario_id(usuario.id)) == Usuario:        
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    else:        
        return agregar_usuario(usuario)
    
@routes.put("/usuario/",  status_code=200)
async def usuario(usuario: Usuario):
    if actualizar_usuario(usuario) == True:
        return actualizar_usuario(usuario)
    else:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    

@routes.delete("/usuario/{id}", status_code=200)
async def usuario(id: int):
    if  eliminar_usuario(id) == True :
        return eliminar_usuario(id)
    else:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")