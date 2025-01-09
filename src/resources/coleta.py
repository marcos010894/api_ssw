from fastapi import APIRouter, Depends
from src.models.ColetarItem import *
from zeep import Client
import xmltodict
import json
from src import crud
from src.dependences.asyncawait import run_in_loop

router = APIRouter(prefix="/coletar", tags=["coletar"])

@router.post("/")
async def coletar(item: ColetarItem):
    response_dict = await run_in_loop(crud.coleta.getColeta, item)
    
    # Retornando a resposta
    return {"response": response_dict}


@router.post('/separate')
async def coletarSeparate(item: ColetarItemSeparate):
    response_dict = await run_in_loop(crud.coleta.getColetaUnicSeparate, item)
    
    # Retornando a resposta
    return {"response": response_dict}
