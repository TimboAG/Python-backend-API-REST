from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
import rutas.rutasProductos as productos
import rutas.rutasUsuarios as usuarios
import rutas.auth_basica_usuario as usuariosAuth
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.include_router(usuarios.routes)
app.include_router(productos.routes)
app.include_router(usuariosAuth.routes)
app.mount("/static", StaticFiles(directory="static"))

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=422)

@app.get("/")
async def root():
    return "Hola"

@app.get("/url")
async def url():
    return {"url": "www.url.com"}