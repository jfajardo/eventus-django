from rest_framework import serializers
from .models import *


class UserMinSerializar(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'avatar')


class EventoMinSerializer(serializers.ModelSerializer):
    usuario = UserMinSerializar(many=False)
    class Meta:
        model = Evento
        fields = ('id', 'nombre', 'observaciones', 'fecha', 'imagen', 'usuario')
