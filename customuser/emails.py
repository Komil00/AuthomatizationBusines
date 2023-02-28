from django.core.mail import send_mail
import random
from django.conf import settings
from .models import CustomUser

def send_code_to_email(email):
    subject = 'Your account verification email'
    code = random.randint(100000, 999999)
    message = f'Your verify code is {code}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj = CustomUser.objects.get(email = email)
    user_obj.code = code
    user_obj.save()