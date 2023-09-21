from aws_xray_sdk.core import xray_recorder , patch_all
from rest_framework import viewsets
from xray.serializer import UserSerializer
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
