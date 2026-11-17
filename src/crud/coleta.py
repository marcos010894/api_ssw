from zeep import Client
import xmltodict
import json


_client = None
_clientSeparate = None

def _get_client():
    global _client
    if _client is None:
        _client = Client('https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')
        _client.service._binding_options['address'] = 'https://ssw.inf.br/ws/sswCotacaoColeta/index.php'
    return _client

def _get_client_separate():
    global _clientSeparate
    if _clientSeparate is None:
        _clientSeparate = Client('https://ssw.inf.br/ws/sswColeta/index.php?wsdl')
        _clientSeparate.service._binding_options['address'] = 'https://ssw.inf.br/ws/sswColeta/index.php'
    return _clientSeparate

def getColeta(item):
    response = _get_client().service.coletar(
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
    response = _get_client_separate().service.coletar(
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
        instrucao=item.instrucao,
        cubagem=item.cubagem,
        valorMerc=item.valorMerc,
        especie=item.especie,
        chaveNF=item.chaveNF,
        cnpjSolicitante=item.cnpjSolicitante,
        nroPedido=item.nroPedido,
        mercadoria=item.mercadoria,
        cepEndColeta=item.cepEndColeta,
        logradouroEndColeta=item.logradouroEndColeta,
        numeroEndColeta=item.numeroEndColeta,
        complementoEndColeta=item.complementoEndColeta,
        bairroEndColeta=item.bairroEndColeta,
        nomeRemetente=item.nomeRemetente,
    )

    # Convertendo XML para dicionário
    response_dict = xmltodict.parse(response)
    
    # Convertendo dicionário para JSON
    response_json = json.dumps(response_dict)
    
    return response_dict