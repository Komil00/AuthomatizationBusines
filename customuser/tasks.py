from AuthomatizationBusines.celery import app
from django.conf import settings
from django.core.mail import send_mail
from .models import CustomUser
# @app.task
# def send_spam_email(email):
    # send_mail(
    #     subject='Add an eye-catching subject',
    #     message='Komil chtu',
    # 	from_email=settings.EMAIL_HOST_USER,
    # 	recipient_list=[email]
    #     )
        
@app.task
def send_beat_email():
    for contact in CustomUser.objects.all():
        send_mail(
            subject='Add an eye-catching subject',
            message=f'{contact.email} chtu man komil',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[contact.email]
        )