from fastapi import FastAPI, HTTPException
from funciones.funcionUsuario import *

app=FastAPI()

@app.get("/usuarios", status_code=200)
async def usuarios():
    return mostrar_usuarios()

#Por path
@app.get("/usuario/{id}", status_code=200)
async def usuario(id:int):
    try:
        return buscar_usuario_id(id)
    except:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    

#Por query
@app.get("/usuario/", status_code=200)
async def usuario(id:int):
    try:
        return buscar_usuario_id(id)
    except:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")

@app.post("/usuario/", status_code=201)
async def usuario(usuario: Usuario):   
    if type(buscar_usuario_id(usuario.id)) == Usuario:        
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    else:        
        return agregar_usuario(usuario)
    
@app.put("/usuario/",  status_code=200)
async def usuario(usuario: Usuario):
    if actualizar_usuario(usuario) == True:
        return actualizar_usuario(usuario)
    else:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")
    

@app.delete("/usuario/{id}", status_code=200)
async def usuario(id: int):
    if  eliminar_usuario(id) == True :
        return eliminar_usuario(id)
    else:
        raise HTTPException(status_code=404, detail="No se encuentra el usuario")