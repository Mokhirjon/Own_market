from django.shortcuts import render
from .models import Clothes
from rest_framework import generics
from .serializers import ClothesSerializers
from config.permissions import AdminPermission
# Create your views here.
class ClothesListAPiviews(generics.ListAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializers
    permission_classes = (AdminPermission,)

class ClothesCreateAPiviews(generics.CreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializers
    permission_classes = (AdminPermission,)

class ClothesUpdateAPiviews(generics.UpdateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializers
    permission_classes = (AdminPermission,)

class ClothesDeleteAPiviews(generics.DestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializers
    permission_classes = (AdminPermission,)

class ClothesDetailsAPiviews(generics.RetrieveAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializers
    permission_classes = (AdminPermission,)