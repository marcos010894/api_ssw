from pydantic import BaseModel

class HtmlString(BaseModel):
    html: str
    assunto: str
    emailSet: str
    
