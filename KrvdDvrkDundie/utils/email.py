import re
import smtplib
from email.mime.text import MIMEText

from KrvdDvrkDundie.settings import SMTP_HOST, SMTP_PORT, SMTP_TIMEOUT
from KrvdDvrkDundie.utils.log import get_logger

log = get_logger()

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def check_valid_email(address):
    """Return email is valid"""
    return bool(re.fullmatch(regex, address))


def send_email(from_, to, subject, text):
    if not isinstance(to, list):
        # raise ValueError("To must be a list") ou
        to = [to]

    try:
        with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT, timeout=SMTP_TIMEOUT) as server:
            message = MIMEText(text)
            message["Subject"] = subject
            message["From"] = from_
            message["To"] = ",".join(to)
            server.sendmail(from_, to, message.as_string())
    except Exception:
        log.error("Cannot send email to %s", to)
