from fastapi import FastAPI,Request
from pydantic import BaseModel
from datetime import datetime
from zeep import Client
from fastapi.middleware.cors import CORSMiddleware
import xmltodict
import json
import pandas as pd
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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



    
@app.get('/getCidades/{uf}/{city}')
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
        
        
@app.get('/tde_verify/{cpf}')
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
    


class HtmlString(BaseModel):
    html: str
    assunto: str
    
@app.post('/setEmail')
def setEmail(html: HtmlString):
    
    html_content = html.html
    # Definindo as credenciais e o servidor SMTP
    smtp_server = "smtp.gmail.com"
    port = 587  # para uso com o servidor do gmail
    username = "dev@salexpress.com.br"
    password = "Mito010894@@"

    # Criando a mensagem
    msg = MIMEMultipart('alternative')
    msg['Subject'] = html.assunto
    msg['From'] = username
    msg['To'] = "email_destino@gmail.com"

    # Criando a parte HTML da mensagem
    html = html_content

    # Adicionando a parte HTML à mensagem
    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    # Conectando ao servidor SMTP e enviando o e-mail
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # saudação opcional, chamada para alguns servidores
        server.starttls()  # segurança
        server.login(username, password)
        server.sendmail(username, "kelder.nagel@salexpress.com.br", msg.as_string())
        server.close()

        print('Email enviado!')
        return {'status': 200, 'mensagem': 'Email enviado!'}
    except Exception as e:
        print('Algo deu errado...', e)
        return e