# from clases.claseUsuario import *
# import db.models.claseUsuario as mi_usuario_db
from db.models.claseUsuario import Usuario
from db.client import db_client
from db.schemas.usuario import usuario_schema, listado_usuarios_schema



def agregar_usuario(usuario: Usuario): 
        # usuario_lista=mostrar_usuarios()  
        # usuario_lista.append(usuario)
        usuario_dicionario=dict(usuario)
        id= db_client.local.usuario.insert_one(usuario_dicionario).inserted_id 
        mi_usuario= buscar_usuario_id(id)
        return mi_usuario

def mostrar_usuarios(): 
    usuario_lista=listado_usuarios_schema(db_client.local.usuario.find())
    return usuario_lista
    
def buscar_usuario_id(id):
    # usuario_lista = mostrar_usuarios()
    # mi_usuario = filter(lambda usuario: usuario.id == id, usuario_lista)
    # mi_usuario = list(mi_usuario)
    mi_usuario=usuario_schema(db_client.local.usuario.find_one({"_id": id}))
    if len(mi_usuario) > 0:
        return Usuario(**mi_usuario)
    else:
        return None
    
def buscar_usuario_email(usuario: str):
    # usuario_lista = mostrar_usuarios()
    # mi_usuario = filter(lambda usuario: usuario.id == id, usuario_lista)
    # mi_usuario = list(mi_usuario)
    mi_usuario=usuario_schema(db_client.local.usuario.find_one({"email": usuario.email}))
    if len(mi_usuario) > 0:
        return Usuario(**mi_usuario)
    else:
        return None   
    
def buscar_usuario(field: str, key):
    # usuario_lista = mostrar_usuarios()
    # mi_usuario = filter(lambda usuario: usuario.id == id, usuario_lista)
    # mi_usuario = list(mi_usuario)
    mi_usuario=usuario_schema(db_client.local.usuario.find_one({field: key}))
    if len(mi_usuario) > 0:
        return Usuario(**mi_usuario)
    else:
        return None  
    
    
def actualizar_usuario(field: str, key, usuario: Usuario):
    usuario_dicionario = dict(usuario)
    del usuario_dicionario["id"]
    usuario_actualizado = db_client.local.usuario.find_one_and_replace(
        {field: key},
        usuario_dicionario,
        return_document=True
    )
    if usuario_actualizado:
        return Usuario(**usuario_schema(usuario_actualizado))
    else:
        return None
    
def eliminar_usuario(field: str, key):  
    mi_usuario= db_client.local.usuario.find_one_and_delete({field: key})
    if not mi_usuario:
        return False
    else:
        return True