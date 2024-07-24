from fastapi import APIRouter, Depends
from src.models.CotarItem import CotarItem
from zeep import Client
import xmltodict
import json
import requests
from datetime import datetime, timedelta
from requests_toolbelt.multipart.encoder import MultipartEncoder

router = APIRouter(prefix="/cotar", tags=["Cotar"])
client = Client('https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')

@router.post("/")
def setEmail(item: linkDownload):
     setEmail_alert()


def setEmail_alert():
        agora = datetime.now()
    
        html_alert = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <style>
                            body {
                                font-family: Arial, sans-serif;
                                background-color: #f4f4f4;
                                color: #333;
                                line-height: 1.6;
                            }
                            .container {
                                max-width: 600px;
                                margin: 20px auto;
                                padding: 20px;
                                background: #fff;
                                border: 1px solid #ddd;
                                border-radius: 5px;
                            }
                            .header {
                                background-color: red;
                                color: #fff;
                                padding: 10px;
                                text-align: center;
                                border-radius: 5px 5px 0 0;
                            }
                            .footer {
                                background-color: black;
                                color: #fff;
                                text-align: center;
                                padding: 5px;
                                border-radius: 0 0 5px 5px;
                            }
                            .content {
                                margin-top: 20px;
                            }
                            .log {
                                font-family: "Courier New", Courier, monospace;
                                background-color: #eee;
                                padding: 10px;
                                margin-top: 20px;
                                overflow-x: auto;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <div class="header">
                                <h1>Relatório Clientes - Simples nacional</h1>
                            </div>
                            <div class="content">
                                <p>Olá,</p>
                                <p>  Segue o relatório dos clientes com o com o simples alterados no dia de ontem.</p>
                                
                            </div>
                            <div class="footer">
                                <p>Atenciosamente,</p>
                                <p>Desenvolvedor salexpress</p>
                            </div>
                        </div>
                    </body>
                    </html>
    """

        api_url = "https://set-email-html-5xpu.vercel.app/upload"
        data_hora = agora.strftime("%d/%m/%Y %H:%M")

        output_filename = 'clientes_atualizado.xlsx'
        multipart_data = MultipartEncoder(
        fields={
            "html_content": html_alert,
            "subject": f'Relatório Clientes - Simples nacional {data_hora}',
            #"to_email": 'marcosmachadodev@gmail.com',
            "to_email": 'kelder.nagel@salexpress.com.br; thais.andrade@salexpress.com.br;  marcosmachadodev@gmail.com',
            # Aqui você deve garantir que o arquivo 'output_filename' é um arquivo .json
            "attachments": ("clientes_atualizado.xlsx", open(output_filename, 'rb'), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        }
        )
        headers = {
            "Content-Type": multipart_data.content_type,
            # Adicione outros cabeçalhos personalizados, se necessário
        }

        response = requests.post(api_url, data=multipart_data, headers=headers)
        if response.status_code == 200:
            print(response.text)
            # Chame sua função setEmailCliente() aqui, se necessário
        else:
            print("Erro ao enviar o e-mail. Código de status:", response.status_code)
            print("Resposta:", response.text)
            destino_artual = []

        return