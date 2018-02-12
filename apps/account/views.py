from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.core.files.base import ContentFile
from .models import *
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
