from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^cambiar-clave$', ChangePassword.as_view()),
    url(r'^cambiar-foto$', UpdateAvatar.as_view()),
]
