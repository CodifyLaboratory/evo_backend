from datetime import date

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


GENDER_CHOICES = [
    ('Male', 'Мужчина'),
    ('Female', 'Женщина'),
]


class User(AbstractUser):
    username = None
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='users-photos/', null=True, blank=True, verbose_name='Фотография')
    email = models.EmailField(verbose_name='Почта', max_length=250, unique=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', default=date.today)
    gender = models.CharField(verbose_name='Пол', max_length=7, choices=GENDER_CHOICES, null=True, blank=True)
    country = models.CharField(verbose_name='Страна', max_length=255, null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Последний вход', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
