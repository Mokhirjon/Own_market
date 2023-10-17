from django.shortcuts import render
from .models import Pants
from .serializers import PantsSerializers
from rest_framework import generics
from config.permissions import AdminPermission
# Create your views here.
class PantsListAPiviews(generics.ListAPIView):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializers
    permission_classes = (AdminPermission,)

class PantsCreateAPiviews(generics.CreateAPIView):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializers
    permission_classes = (AdminPermission,)

class PantsUpdateAPiviews(generics.UpdateAPIView):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializers
    permission_classes = (AdminPermission,)

class PantsDeleteAPiviews(generics.DestroyAPIView):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializers
    permission_classes = (AdminPermission,)
class PantsDetailsAPiviews(generics.RetrieveAPIView):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializers
    permission_classes = (AdminPermission,)
