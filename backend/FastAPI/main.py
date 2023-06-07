from fastapi import FastAPI
import rutas.rutasProductos as productos
import rutas.rutasUsuarios as usuarios

app=FastAPI()

app.include_router(usuarios.routes)
app.include_router(productos.routes)

@app.get("/")
async def root():
    return "Hola"

@app.get("/url")
async def url():
    return {"url": "www.url.com"}