from pydantic import BaseModel

class Usuario(BaseModel):
    nombre_usuario: str
    nombre_completo: str
    email: str
    activo: bool

class UsuarioDb(Usuario):
    contraseña: str

usuario_db={
    "usuario1":{
        "nombre_usuario": "usuario1",
        "nombre_completo": "nombre1 apellido1",
        "email": "usuario1@gmail.com",
        "activo": True,
        "contraseña": "$2a$12$G7kz4QDbjRqvSMjuRkb6vu.p8vTZsMcL5uUj3fyJ7JFowZfTPChH."
    },
    "usuario2":{
        "nombre_usuario": "usuario2",
        "nombre_completo": "nombre2 apellido2",
        "email": "usuario2@gmail.com",
        "activo": False,
        "contraseña": "usuario2"
    }
}
    
        