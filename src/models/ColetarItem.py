from pydantic import BaseModel
from datetime import datetime

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



class ColetarItemSeparate(BaseModel):
    dominio: str
    login: str
    senha: str
    cnpjRemetente: str
    cnpjDestinatario: str
    tipoPagamento: str
    cepEntrega: str
    solicitante: str
    limiteColeta: datetime
    quantidade: int
    peso: float
    numeroNF: str
    enderecoEntrega: str
    observacao: str
    instrucao: str
    cubagem: float
    valorMerc: float
    especie: str
    chaveNF: str
    cnpjSolicitante: str
    nroPedido: str