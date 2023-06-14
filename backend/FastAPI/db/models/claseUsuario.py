from pydantic import BaseModel

class Usuario(BaseModel):
    id: str | None
    nombre_usuario: str
    nombre_completo: str
    email: str
    activo: bool