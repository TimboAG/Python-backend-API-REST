from pydantic import BaseModel

class Usuario(BaseModel):
    nombre_usuario: str
    nombre_completo: str
    email: str
    activo: bool