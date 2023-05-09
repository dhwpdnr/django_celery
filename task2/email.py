from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import ssl
from django.core.mail import get_connection


def send_review_email(name, email, review):
    context = {
        'name': name,
        'email': email,
        'review': review
    }
    connection = get_connection(
        ssl_certfile=None,
        ssl_keyfile=None,
        ssl_cert_reqs=ssl.CERT_NONE,
        ssl_ca_certs=None,
        timeout=None,
    )

    email_subject = 'Thank you for your review'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    return email.send(fail_silently=False)
