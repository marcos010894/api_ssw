from fastapi import APIRouter, Depends
from src.models.ColetarItem import ColetarItem
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
