from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from zeep import Client
from fastapi.middleware.cors import CORSMiddleware
import xmltodict
import json

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Criando um cliente com a URL do WSDL
client = Client('https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')

class CotarItem(BaseModel):
    dominio: str
    login: str
    senha: str
    cnpjPagador: str
    cepOrigem: int
    cepDestino: int
    valorNF: float
    quantidade: int
    peso: float
    volume: float
    mercadoria: int
    ciffob: str
    cnpjRemetente: str
    cnpjDestinatario: str
    observacao: str
    trt: str
    coletar: str
    entDificil: str
    destContribuinte: str

@app.get('/')
def respo():
    return {"resposta": "ok"}
@app.post("/cotar")
def cotar(item: CotarItem):
    # Chamando a função desejada e passando os parâmetros necessários
    response = client.service.cotar(
        dominio=item.dominio,
        login=item.login,
        senha=item.senha,
        cnpjPagador=item.cnpjPagador,
        cepOrigem=item.cepOrigem,
        cepDestino=item.cepDestino,
        valorNF=item.valorNF,
        quantidade=item.quantidade,
        peso=item.peso,
        volume=item.volume,
        mercadoria=item.mercadoria,
        ciffob=item.ciffob,
        cnpjRemetente=item.cnpjRemetente,
        cnpjDestinatario=item.cnpjDestinatario,
        observacao=item.observacao,
        trt=item.trt,
        coletar=item.coletar,
        entDificil=item.entDificil,
        destContribuinte=item.destContribuinte,
    )
    
     # Convertendo XML para dicionário
    response_dict = xmltodict.parse(response)
    
    # Convertendo dicionário para JSON
    response_json = json.dumps(response_dict)
    
    # Retornando a resposta
    return {"response": response_dict}

class ColetarItem(BaseModel):
    dominio: str
    login: str
    senha: str
    cotacao: int
    limiteColeta: datetime
    token: str
    solicitante: str
    observacao: str
    chaveNFe: str
    nroPedido: str

@app.post("/coletar")
def coletar(item: ColetarItem):
    # Chamando a função desejada e passando os parâmetros necessários
    response = client.service.coletar(
        dominio=item.dominio,
        login=item.login,
        senha=item.senha,
        cotacao=item.cotacao,
        limiteColeta=item.limiteColeta,
        token=item.token,
        solicitante=item.solicitante,
        observacao=item.observacao,
        chaveNFe=item.chaveNFe,
        nroPedido=item.nroPedido,
    )

    # Convertendo XML para dicionário
    response_dict = xmltodict.parse(response)
    
    # Convertendo dicionário para JSON
    response_json = json.dumps(response_dict)
    
    # Retornando a resposta
    return {"response": response_dict}
