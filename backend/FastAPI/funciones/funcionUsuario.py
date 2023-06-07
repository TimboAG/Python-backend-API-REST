from clases.claseUsuario import *


def agregar_usuario(usuario: Usuario): 
        usuario_lista=mostrar_usuarios()      
        usuario_lista.append(usuario)
        return usuario

def mostrar_usuarios():    
    usuario_lista=[Usuario(id=1,nombre="Usuario1", apellido="apellido1", url= "url1", edad=1),
                Usuario(id=2,nombre="Usuario2", apellido="apellido2", url= "url2", edad=2),
                Usuario(id=3,nombre="Usuario3", apellido="apellido3", url= "url3", edad=3)]
    return usuario_lista
    
def buscar_usuario_id(id):
    usuario_lista = mostrar_usuarios()
    mi_usuario = filter(lambda usuario: usuario.id == id, usuario_lista)
    mi_usuario = list(mi_usuario)
    if len(mi_usuario) > 0:
        return mi_usuario[0]
    else:
        return None   
    
def actualizar_usuario(usuario: Usuario):
    usuario_lista=mostrar_usuarios()
    usuario_encontrado= False
    for index, modifica_usuario in enumerate(usuario_lista):
        if modifica_usuario.id== usuario.id:
            usuario_lista[index]=usuario
            usuario_encontrado= True
            
    return usuario_encontrado 
    
def eliminar_usuario(id: int):
    usuario_lista=mostrar_usuarios()
    usuario_encontrado= False
    for index, modifica_usuario in enumerate(usuario_lista):
        if modifica_usuario.id== id:
            del usuario_lista[index]
            usuario_encontrado= True
            
    return usuario_encontrado