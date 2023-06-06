from clases.claseUsuario import *

def mostrar_usuarios():    
    usuario_lista=[Usuario(id=1,nombre="Usuario1", apellido="apellido1", url= "url1", edad=1),
                Usuario(id=2,nombre="Usuario2", apellido="apellido2", url= "url2", edad=2),
                Usuario(id=3,nombre="Usuario3", apellido="apellido3", url= "url3", edad=3)]
    return usuario_lista
    
def buscar_usuario_id(id):
    usuario_lista=mostrar_usuarios()
    try:
        mi_usuario = filter(lambda usuario: usuario.id == id, usuario_lista)
        return list(mi_usuario)[0]
    except:
        return {"error": "No se encuentra el usuario"}