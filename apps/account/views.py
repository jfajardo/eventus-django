from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django.core.files.base import ContentFile
from .models import *
from .serializers import *
import string
import random
import base64


class ChangePassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            chars = string.ascii_uppercase + string.digits
            password = "".join(random.choice(chars) for x in range(1, 8))
            user = User.objects.get(email=request.data['email'])
            user.set_password(password)
            user.save()
            return Response({'actualizado': True, 'mensaje': password})
        except Exception as e:
            return Response({'actualizado': False, 'mensaje':'Email no registrado!'})


class UpdateAvatar(APIView):

    def put(self, request):
        try:
            image_data = base64.b64decode(request.data['foto'])
            request.user.avatar = ContentFile(image_data, '{0}.jpg'.format(request.user))
            request.user.save()
            return Response({'actualizado': True})
        except Exception as e:
            return Response({'actualizado': False})


class EventosList(ListAPIView):
    serializer_class = EventoMinSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def get_queryset(self):
        eventos = Evento.objects.all()
        return eventos


class EventoView(APIView):

    def post(self, request):
        try:
            request.data['usuario'] = request.user.id
            request.data['latitud'] = 0
            request.data['longitud'] = 0
            serializer = EventoSerializer(data=request.data)
            if serializer.is_valid():
                evento = serializer.save()
                print(evento)
                image_data = base64.b64decode(request.data['imagen'])
                evento.imagen = ContentFile(image_data, '{0}.jpg'.format(request.user))
                evento.save()
                print(serializer.errors)
                evento_s = EventoMinSerializer(evento, many=False)
                return Response(evento_s.data)
        except Exception as e:
            print(e)
            return Response({'agregado': False})


class EventoDeleteView(APIView):

    def delete(self, request, id):
        try:
            Evento.objects.get(id=id, usuario=request.user).delete()
            return Response({'eliminado': True})
        except Exception as e:
            print(e)
            return Response({'eliminado': False})
