from fastapi import FastAPI, APIRouter, HTTPException, UploadFile, File, Form, BackgroundTasks
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import asyncio
from typing import List

app = FastAPI()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "dev@salexpress.com.br"
SMTP_PASSWORD = "@@Mito010894"

router = APIRouter(prefix="/setEmail", tags=["setEmail"])

# Crie uma única conexão SMTP persistente
smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp_server.starttls()
smtp_server.login(SMTP_USER, SMTP_PASSWORD)

@router.post("/")
async def send_email_endpoint(
    background_tasks: BackgroundTasks,
    subject: str = Form(...),
    to_email: str = Form(...),
    html_content: str = Form(...),
    attachments: List[UploadFile] = File(...)
):
    background_tasks.add_task(sendemail, subject, to_email, html_content, attachments)
    return 'ok'

async def send_email(subject: str, to_email: str, html_content: str, attachments: List[UploadFile] = []):
    # msg = MIMEMultipart('alternative')
    # msg['Subject'] = subject
    # msg['From'] = SMTP_USER
    # msg['To'] = to_email

    # # Attach HTML content
    # msg.attach(MIMEText(html_content, 'html'))

    # for attachment in attachments:
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload(attachment.file.read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', f'attachment; filename= {attachment.filename}')
    #     msg.attach(part)

    # # Envie o email usando a conexão SMTP persistente
    # smtp_server.sendmail(SMTP_USER, to_email, msg.as_string())
    return
    
    
async def sendemail(subject,
            to_email,
            html_content,
            attachments):
    try:
        await asyncio.gather(
            send_email(subject, to_email, html_content, attachments)
        )
        return {"status": 200, "message": "Email sent successfully!"}
    except Exception as e:
        pass