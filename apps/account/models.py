from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
import datetime

class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, username, email, first_name, last_name, password,
                     is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          first_name=first_name, last_name=last_name,
                          is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(
            username,
            email,
            first_name,
            last_name,
            password,
            False,
            False,
            **extra_fields
        )

    def create_superuser(self, username, email, first_name, last_name, password=None):
        return self._create_user(
            username, email, first_name, last_name, password, True, True
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    avatar = models.ImageField(upload_to='users',
                               default='users/user_avatar.jpg', blank=True)
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'avatar']

    class Meta:
        ordering = ('first_name', 'last_name')

    def __unicode__(self):
        return self.get_full_name()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        if not self.last_name or not self.first_name:
            return self.username
        else:
            return self.first_name + ' ' + self.last_name


class Evento(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    fecha = models.DateTimeField(blank=True, default=datetime.datetime.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos')
    direccion = models.CharField(blank=True, max_length=100)
    observaciones = models.TextField(blank=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.ImageField(upload_to='eventos',
                               default='eventos/no_foto.png', blank=True)

    def __unicode__(self):
        return self.nombre
