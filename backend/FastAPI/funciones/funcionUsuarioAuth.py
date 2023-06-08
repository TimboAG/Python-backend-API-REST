from clases.claseUsuarioAuth import *
from excepciones.excepcion import *


def buscar_usuario(nombre_usuario: str):
    if nombre_usuario in usuario_db:
        return UsuarioDb(**usuario_db[nombre_usuario])


def verificar_usuario(username, password):
    usuario = usuario_db.get(username)
    if not usuario:
        raise UsuarioNoEncontradoException()
    if not password == usuario.contraseña:
        raise ContraseñaIncorrectaException()
    return {"access_token": usuario.nombre_usuario, "token_type": "bearer"}



