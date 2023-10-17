from django.shortcuts import render
from .models import Shoes,Shopping_center
from .serializers import ShoesSerializers,Shopping_centerSerializers
from rest_framework import generics
from config.permissions import AdminPermission
# Create your views here.

class Shopping_centerListCreateAPiviews(generics.ListCreateAPIView):
    queryset = Shopping_center.objects.all()
    serializer_class = Shopping_centerSerializers
    permission_classes = (AdminPermission,)
class ShoesListAPiviews(generics.ListAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializers
    permission_classes = (AdminPermission,)
class ShoesCreateAPiviews(generics.CreateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializers
    permission_classes = (AdminPermission,)
class ShoesUpdateAPiviews(generics.UpdateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializers
    permission_classes = (AdminPermission,)
class ShoesDeleteAPiviews(generics.DestroyAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializers
    permission_classes = (AdminPermission,)
class ShoesDetailsAPiviews(generics.RetrieveAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializers
    permission_classes = (AdminPermission,)