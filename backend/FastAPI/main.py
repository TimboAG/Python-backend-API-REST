from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return "Hola"

@app.get("/url")
async def url():
    return {"url": "www.url.com"}