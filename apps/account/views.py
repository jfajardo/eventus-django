from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import *
import string
import random


class ChangePassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            chars = string.ascii_uppercase + string.digits
            password = "".join(random.choice(chars) for x in range(1, 8))
            print(password)
            user = User.objects.get(email=request.data['email'])
            user.set_password(password)
            user.save()
            return Response({'actualizado': True, 'mensaje': password})
        except Exception as e:
            return Response({'actualizado': False, 'mensaje':'Email no registrado!'})
