from emails.service import EmailService
from django.core import mail


def test_send_activation_link() -> None:
    username = "user"
    email = "user@example.com"

    EmailService.send_activation_link(
        username=username,
        email=email,
    )

    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == "Activate your account"
    assert mail.outbox[0].to == [email]
