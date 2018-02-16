from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^cambiar-clave$', ChangePassword.as_view()),
    url(r'^cambiar-foto$', UpdateAvatar.as_view()),
    url(r'^eventos$', EventosList.as_view()),
    url(r'^evento$', EventoView.as_view()),
]
