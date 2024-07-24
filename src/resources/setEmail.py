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


@router.post("/")
async def send_email_endpoint(
    subject: str = Form(...),
    to_email: str = Form(...),
    html_content: str = Form(...),
    attachments: List[UploadFile] = File(...)
):
  return

async def send_email(subject: str, to_email: str, html_content: str, attachments: List[UploadFile] = []):
   return