from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from dataclasses import dataclass
from datetime import datetime


@dataclass
class EmailService:

    @staticmethod
    def send_activation_link(username: str, email: str) -> None:
        timestamp = datetime.now().timestamp() * 1000 + 120000

        email_body = render_to_string(
            "activation_email.html",
            {
                "username": username,
                "timestamp": timestamp,
            },
        )

        email = EmailMessage(
            subject="Activate your account",
            body=email_body,
            to=[email],
        )
        email.content_subtype = "html"
        email.send()
