from fastapi import FastAPI
from rutas import rutasUsuario

app=FastAPI()

app.include_router(rutasUsuario.routes)

@app.get("/")
async def root():
    return "Hola"

@app.get("/url")
async def url():
    return {"url": "www.url.com"}