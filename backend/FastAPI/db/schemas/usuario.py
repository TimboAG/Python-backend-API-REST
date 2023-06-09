def usuario_schema(usuario) -> dict:
    if usuario is None:
        return {}
    return {
        "id": str(usuario["_id"]),
        "nombre_usuario": usuario["nombre_usuario"],
        "nombre_completo": usuario["nombre_completo"],
        "email": usuario["email"],
        "activo": usuario["activo"]
    }
    
def listado_usuarios_schema(usuarios):
    return [usuario_schema(usuario) for usuario in usuarios]