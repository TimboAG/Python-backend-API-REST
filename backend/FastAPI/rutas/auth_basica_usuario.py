from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from funciones.funcionUsuarioAuth import *
from excepciones.excepcion import *

oauth2= OAuth2PasswordBearer(tokenUrl="login")
routes=APIRouter()
async def current_user(token:str= Depends(oauth2) ):
    usuario= buscar_usuario(token)


@routes.post("/login", status_code=200)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    try:
        username = form.username
        password= form.password
        return verificar_usuario(username, password)
    except UsuarioNoEncontradoException:
        raise HTTPException(status_code=404, detail=MENSAJE_USUARIO_NO_ENCONTRADO)
    except ContraseñaIncorrectaException:
        raise HTTPException(status_code=401, detail=MENSAJE_CONTRASEÑA_INCORRECTA)
    except:
        raise HTTPException(status_code=500, detail="Ocurrió un error desconocido")