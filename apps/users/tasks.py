from django.core.mail import send_mail

from core.celery import app
from celery import shared_task

@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(subject, message, "azizjon1708@gmail.com", recipient_list)
