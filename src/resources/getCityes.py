from fastapi import APIRouter, Depends
from src.models.ColetarItem import ColetarItem
from zeep import Client
import xmltodict
import json
import pandas as pd

router = APIRouter(prefix="/getCidades", tags=["getCidades"])
client = Client('https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')

@router.get("/{uf}/{city}")
    
def getCidades(city:str, uf: str):
    # Carrega o arquivo Excel
    df = pd.read_excel('Cidades Vs Unidades.xlsx')

    # Converte os dados em JSON
    json_data = df.to_json(orient='records')
   # Salvar em um arquivo JSON
    with open('datacities.json', 'w') as file: #Sempre quando converter um excel para json lembrar e salvar em um arquivo.json para dar certo...
        file.write(json_data)
    # Abrir o arquivo JSON
    docSave = {}
    returned = False
    with open('datacities.json', 'r') as file:
        json_data1 = json.load(file)
        for doc in json_data1:
           if doc['CIDADE'] == city and doc['UF'] == uf:
                docSave = doc
                returned = True
    if returned:
        return docSave
    else:
        return {'erro': 'nenhum dado encontrado...'}
        