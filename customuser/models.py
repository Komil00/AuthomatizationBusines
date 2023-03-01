from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

USERS_CHOICES= [
    ('Diller', "Diller"),
    ('Client', "Client"),
 ]

class CustomUser(AbstractUser):
    who = models.CharField(max_length=15, choices=USERS_CHOICES, default=USERS_CHOICES[0])
    username = models.CharField(max_length=20, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    phone_regex = RegexValidator(regex=r'^\+?998?\d{9}$', message="Phone number must be entered in the format: '+998********'. Up to 12w digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    avatar = models.ImageField(upload_to='avatar')
    is_verify = models.BooleanField(default=False)
    code = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


