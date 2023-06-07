from fastapi import FastAPI
import rutas.rutasProductos as productos
import rutas.rutasUsuarios as usuarios
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.include_router(usuarios.routes)
app.include_router(productos.routes)
app.mount("/static", StaticFiles(directory="static"))

@app.get("/")
async def root():
    return "Hola"

@app.get("/url")
async def url():
    return {"url": "www.url.com"}