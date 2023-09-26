from fastapi import FastAPI, APIRouter, HTTPException, UploadFile, File, Form
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import asyncio
from typing import List
import os
from dotenv import load_dotenv
app = FastAPI()

# Carregue as variáveis de ambiente do arquivo .env
load_dotenv()


SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
router = APIRouter(prefix="/setEmail", tags=["setEmail"])

# Crie uma única conexão SMTP persistente
smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp_server.starttls()
smtp_server.login(SMTP_USER, SMTP_PASSWORD)

@router.post("/")
async def send_email_endpoint(
    subject: str = Form(...),
    to_email: str = Form(...),
    html_content: str = Form(...),
    attachments: List[UploadFile] = File(...)
):
    try:
        await asyncio.gather(
            send_email(subject, to_email, html_content, attachments)
        )
        return {"status": 200, "message": "Email sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

async def send_email(subject: str, to_email: str, html_content: str, attachments: List[UploadFile] = []):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = to_email

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    for attachment in attachments:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment.filename}')
        msg.attach(part)

    # Envie o email usando a conexão SMTP persistente
    smtp_server.sendmail(SMTP_USER, to_email, msg.as_string())