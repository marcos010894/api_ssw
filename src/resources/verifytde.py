from fastapi import APIRouter, Depends
from src.models.ColetarItem import ColetarItem
from zeep import Client
import xmltodict
import json
import pandas as pd

router = APIRouter(prefix="/tde_verify", tags=["tde_verify"])
client = Client('https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')

@router.get("/{cpf}")
def getTde(cpf:int):
   
    df = pd.read_excel('tde.xlsx')

    json_data = df.to_json(orient='records')
    with open('tde.json', 'w') as file:
        file.write(json_data)
   
    with open('tde.json', 'r') as file:
        json_data1 = json.load(file)
        for doc in json_data1:
           if doc['CNPJ/CPF'] == cpf:
                return {'entrega_dificil':'s'}
    
        return {'entrega_dificil':'n'}