from fastapi import APIRouter, Depends
from src.models.ColetarItem import ColetarItem
from zeep import Client
import xmltodict
import json
import pandas as pd

router = APIRouter(prefix="/unidadeX", tags=["unidadeX"])
client = Client('https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')

@router.get("/{unidade}")
def getEmail(unidade: str):
    df = pd.read_excel('Bases-gerentes-cidades.xlsx')
    if unidade == 'VGE':
        unidade = 'VGA'

    json_data = df.to_json(orient='records')
    with open('bases_email.json', 'w') as file:
        file.write(json_data)
   
    with open('bases_email.json', 'r') as file:
        json_data1 = json.load(file)
        for doc in json_data1:
           if doc['UNIDADE'] == unidade:
               return doc    
        return {'entrega_dificil':'n'}
    