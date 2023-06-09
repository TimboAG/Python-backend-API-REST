from clases.claseUsuarioAuth import *
from excepciones.excepcion import *
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

ALGORITM0="HS256"
crypt= CryptContext(schemes=["bcrypt"])
ACCESS_TOKE_DURACION=1
SECRET="esteEsMiSecreto"

def buscar_usuario(nombre_usuario: str):
    if nombre_usuario in usuario_db:
        return UsuarioDb(**usuario_db[nombre_usuario])
    
def verificar_usuario(username, password):
    mi_usuario_db = usuario_db.get(username)
    if not mi_usuario_db:
        raise UsuarioNoEncontradoException()
    mi_usuario= buscar_usuario(username)    
    if not crypt.verify(password, mi_usuario.contraseña):
        raise ContraseñaIncorrectaException()    
    access_token_expiracion= datetime.utcnow() + timedelta(minutes=ACCESS_TOKE_DURACION)  
    access_token= {"sub": mi_usuario.nombre_usuario,"exp": access_token_expiracion}
    return {"acces_token": jwt.encode(access_token,SECRET, algorithm=ALGORITM0), "token_type": "bearer"}

