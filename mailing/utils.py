from django import template
from django.conf import settings
from django.core.mail import send_mail

from clients.models import Client
from mailing.models import Mailing, Message

register = template.Library()


def send_email(*args):
    all_email = []

    for client in Client.objects.all():
        all_email.append(str(client.email))

    for mailing in Mailing.objects.all():
        if mailing.status == Mailing.STATUS.CREATED and mailing.period == (str(*args)):
            filtered_message = mailing.message
            message = Message.objects.filter(subject=filtered_message)

            for msg in message:
                send_mail(
                    subject=msg.subject,
                    message=msg.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*all_email],
                )
                status_list = []

                for status in Mailing.objects.all():
                    if status.status == Mailing.STATUS.RUNNING:
                        status_list.append(status)

                if not status_list:
                    mailing.status = Mailing.STATUS.COMPLETED
                    mailing.save()
