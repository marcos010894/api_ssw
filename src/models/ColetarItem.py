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