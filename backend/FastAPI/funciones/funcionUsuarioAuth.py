from clases.claseUsuarioAuth import *

def buscar_usuario(nombre_usuario: str):
    if nombre_usuario in usuario_db:
        return UsuarioDb(usuario_db[nombre_usuario])
