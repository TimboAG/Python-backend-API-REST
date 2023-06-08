MENSAJE_USUARIO_NO_ENCONTRADO = "El usuario no fue encontrado"
MENSAJE_CONTRASEÑA_INCORRECTA = "La contraseña no es correcta"


class UsuarioNoEncontradoException(Exception):
    def __init__(self, mensaje=MENSAJE_USUARIO_NO_ENCONTRADO):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ContraseñaIncorrectaException(Exception):
    def __init__(self, mensaje=MENSAJE_CONTRASEÑA_INCORRECTA):
        self.mensaje = mensaje
        super().__init__(self.mensaje)