from fastapi import APIRouter, HTTPException
from funciones.funcionUsuario import *
from db.models.claseUsuario import Usuario

routes=APIRouter(prefix="/usuario",tags=["usuario"], responses={404: {"message": "No encontrado"}})

@routes.get("/", status_code=200)
async def usuarios():
    try:
        return mostrar_usuarios()
    except:
        raise HTTPException(status_code=404, detail="Ocurrio un error")

#Por path
@routes.get("/{id}", status_code=200)
async def usuario(id:int):
    try:
        return buscar_usuario_id(id)
    except:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    

#Por query
@routes.get("/", status_code=200)
async def usuario(id:int):
    try:
        return buscar_usuario_id(id)
    except:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")

@routes.post("/", status_code=201)
async def usuario(usuario: Usuario):   
    if type(buscar_usuario_email(usuario)) == Usuario:        
        raise HTTPException(status_code=404, detail="El  usuario ya se encuentra registrado")
    else:        
        return agregar_usuario(usuario)
    
@routes.put("/",  status_code=200)
async def usuario(usuario: Usuario):
    if actualizar_usuario(usuario) == True:
        return actualizar_usuario(usuario)
    else:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    

@routes.delete("/{id}", status_code=200)
async def usuario(id: int):
    if  eliminar_usuario(id) == True :
        return eliminar_usuario(id)
    else:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")