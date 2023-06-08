from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from funciones.funcionUsuarioAuth import *
from excepciones.excepcion import *

routes=APIRouter()
oauth2= OAuth2PasswordBearer(tokenUrl="login")


async def current_user(token:str= Depends(oauth2) ):
    usuario= buscar_usuario(token)
    if not usuario:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticacion invalidas", 
                            headers={"WWW-Authenticate": "Bearer"})
    if usuario.activo:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo")        
    return usuario
        


@routes.post("/login", status_code=200)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    try:
        username = form.username
        password= form.password
        return verificar_usuario(username, password)
    except UsuarioNoEncontradoException:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=MENSAJE_USUARIO_NO_ENCONTRADO)
    except ContraseñaIncorrectaException:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=MENSAJE_CONTRASEÑA_INCORRECTA)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ocurrió un error desconocido")
    
@routes.get("/usuarios/me", status_code=200)
async def me(usuario: Usuario = Depends(current_user)): 
    return usuario