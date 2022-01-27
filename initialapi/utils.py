import os
import secrets
import smtplib
import string
import random
from email.message import EmailMessage


class SendMessageFromEmail:
    def __init__(self, sender_email, sender_email_password):
        self.sender = sender_email
        self.password = sender_email_password
        self.port = os.environ.get('PORT')
        self.server = os.environ.get('SERVER')

    def send_message(self, receiver: str, subject: str, message: str) -> None:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = receiver
        msg.set_content(message)

        with smtplib.SMTP_SSL(self.server, int(self.port)) as smtp:
            smtp.login(self.sender, self.password)
            smtp.send_message(msg)


def generate_password(length=15):
    alphabet = string.ascii_letters + string.digits + '!@#$^&*()_+='
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def generate_code(length=5):
    return random.randint(10**length, 10**(length+1))


def replace_email_symbols_to_asterisks(email: str):
    return email.replace(email[2: len(email) - 12], '*'*2)
