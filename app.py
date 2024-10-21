from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.resources import cotar, coleta, getCityes, verifytde, unidade, setEmail


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def respo():
    return {"resposta": "ok"}

app.include_router(cotar.router)
app.include_router(coleta.router)
app.include_router(getCityes.router)
app.include_router(verifytde.router)
app.include_router(unidade.router)
app.include_router(setEmail.router)