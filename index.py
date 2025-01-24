from fastapi import FastAPI
from app import node
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')


app.include_router(node)
