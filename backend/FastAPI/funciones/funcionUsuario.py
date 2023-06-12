from clases.claseUsuario import *
import db.models.claseUsuario as mi_usuario_db
from db.client import db_client



def agregar_usuario(usuario: Usuario): 
        # usuario_lista=mostrar_usuarios()  
        # usuario_lista.append(usuario)
        usuario_dicionario=dict(Usuario)
        id= db_client.local.usuario.insert_one(usuario_dicionario).inserted_id 
        return usuario

def mostrar_usuarios(): 
    # db_client.local.usuario   
    usuario_lista=[]
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