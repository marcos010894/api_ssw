from fastapi import APIRouter, Depends
from src.models.CotarItem import CotarItem
from zeep import Client
import xmltodict
import json


router = APIRouter(prefix="/cotar", tags=["Cotar"])
client = Client('https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')
clientMoTable = Client('https://ssw.inf.br/ws/sswCotacao/index.php?wsdl')

@router.post("/")
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
        qtdePares=0,
        altura=0,
        comprimento=0, 
        largura=0,
        fatorMultiplicador=0
    )
    
     # Convertendo XML para dicionário
    response_dict = xmltodict.parse(response)
    
    # Convertendo dicionário para JSON
    response_json = json.dumps(response_dict)
    
    # Retornando a resposta
    return {"response": response_dict}


@router.post("/no-table")
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
        qtdePares=0,
        altura=0,
        comprimento=0, 
        largura=0,
        fatorMultiplicador=0
    )
    
     # Convertendo XML para dicionário
    response_dict = xmltodict.parse(response)
    
    # Convertendo dicionário para JSON
    response_json = json.dumps(response_dict)
    
    # Retornando a resposta
    return {"response": response_dict}