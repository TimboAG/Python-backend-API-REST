from clases.claseUsuarioAuth import *
from excepciones.excepcion import *


def buscar_usuario(nombre_usuario: str):
    if nombre_usuario in usuario_db:
        return UsuarioDb(usuario_db[nombre_usuario])
    
def verificar_usuario(username, password):
    mi_usuario_db = usuario_db.get(username)
    if not mi_usuario_db:
        raise UsuarioNoEncontradoException()
    mi_usuario= buscar_usuario(username)
    if not password == mi_usuario.contraseña:
        raise ContraseñaIncorrectaException()
    return {"acces_token": mi_usuario.nombre_usuario, "token_type": "bearer"}

