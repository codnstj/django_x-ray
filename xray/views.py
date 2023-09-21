from aws_xray_sdk.core import xray_recorder , patch_all
from rest_framework import viewsets
from xray.serializer import UserSerializer
from django.contrib.auth.models import User

segment = xray_recorder.begin_segment('ViewSets')

class UserViewSet(viewsets.ModelViewSet):
    subsegment = xray_recorder.begin_subsegment('UserViewSet')
    queryset = User.objects.all()
    serializer_class = UserSerializer

xray_recorder.end_subsegment()
xray_recorder.end_segment()
