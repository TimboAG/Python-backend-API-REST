from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    apellido: str
    url: str
    edad: int