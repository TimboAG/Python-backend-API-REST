from fastapi import APIRouter, HTTPException
from funciones.funcionUsuario import *
from db.models.claseUsuario import Usuario
from typing import List
from bson import ObjectId


routes=APIRouter(prefix="/usuario",tags=["usuario"], responses={404: {"message": "No encontrado"}})

@routes.get("/", status_code=200, response_model=List[Usuario])
async def usuarios():
    try:
        return mostrar_usuarios()
    except:
        raise HTTPException(status_code=404, detail="Ocurrió un error")

#Por path
@routes.get("/{id}", status_code=200)
async def usuario(id:str):
    try:
        return buscar_usuario("_id", ObjectId(id)  )
    except:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    

#Por query
@routes.get("/", status_code=200)
async def usuario(id:str):
    try:
        return buscar_usuario("_id", ObjectId(id)  )
    except:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")

@routes.post("/", status_code=201)
async def usuario(usuario: Usuario):   
    if type(buscar_usuario_email(usuario)) == Usuario:        
        raise HTTPException(status_code=404, detail="El  usuario ya se encuentra registrado")
    else:        
        return agregar_usuario(usuario)
    
@routes.put("/", status_code=200, response_model=Usuario)
async def usuario(usuario: Usuario):
    usuario_actualizado = actualizar_usuario("_id", ObjectId(usuario.id), usuario)
    if usuario_actualizado:
        return usuario_actualizado
    else:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    

@routes.delete("/{id}", status_code=200)
async def usuario(id: str):
    if  eliminar_usuario("_id", ObjectId(id)) == True :
        eliminar_usuario("_id", ObjectId(id))         
        return HTTPException(status_code=200, detail="Se elimino correctamente el usuario")    
    else:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")