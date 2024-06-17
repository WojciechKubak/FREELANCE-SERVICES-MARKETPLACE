from django.core.mail import EmailMessage
from dataclasses import dataclass
from datetime import datetime


@dataclass
class EmailService:

    @staticmethod
    def send_activation_link(username: str, email: str) -> None:
        timestamp = datetime.now().timestamp() * 1000 + 120000

        email_body = f"""\
            <html>
                <body>
                    <div>
                        <h1>Hello {username}!</h1>
                        <h2>Activate your account</h2>
                        <h3>http://localhost:80/auth/activate?username={username}&timestamp={timestamp}</h3>
                    </div>
                </body>
            </html>
        """

        email = EmailMessage(
            subject="Activate your account",
            body=email_body,
            to=[email],
        )
        email.content_subtype = "html"
        email.send()
