from zeep import Client
import xmltodict
import json


client = Client('https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')
clientSeparate = Client('https://ssw.inf.br/ws/sswColeta/index.php?wsdl')

def getColeta(item):
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
    
    return response_dict



def getColetaUnicSeparate(item):
    response = clientSeparate.service.coletar(
        dominio=item.dominio,
        login=item.login,
        senha=item.senha,
        cnpjRemetente=item.cnpjRemetente,
        cnpjDestinatario=item.cnpjDestinatario,
        tipoPagamento=item.tipoPagamento,
        cepEntrega=item.cepEntrega,
        solicitante=item.solicitante,
        limiteColeta=item.limiteColeta,
        quantidade=item.quantidade,
        peso=item.peso,
        numeroNF=item.numeroNF,
        enderecoEntrega=item.enderecoEntrega,
        observacao=item.observacao,
        instrucao=item.instrucao
    )

    # Convertendo XML para dicionário
    response_dict = xmltodict.parse(response)
    
    # Convertendo dicionário para JSON
    response_json = json.dumps(response_dict)
    
    return response_dict