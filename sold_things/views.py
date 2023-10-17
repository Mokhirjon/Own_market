from django.shortcuts import render
from .serializers import Sold_outSerializers
from .models import Sold_out
from rest_framework import generics
from config.permissions import AdminPermission
# Create your views here.
class Sold_outListapieview(generics.ListAPIView):
    queryset = Sold_out.objects.all()
    serializer_class = Sold_outSerializers
    permission_classes = (AdminPermission,)


class Sold_outcreateapieview(generics.CreateAPIView):
    queryset = Sold_out.objects.all()
    serializer_class = Sold_outSerializers
    permission_classes = (AdminPermission,)


class Sold_outupdateapieview(generics.UpdateAPIView):
    queryset = Sold_out.objects.all()
    serializer_class = Sold_outSerializers
    permission_classes = (AdminPermission,)

class Sold_outdeleteapieview(generics.DestroyAPIView):
    queryset = Sold_out.objects.all()
    serializer_class = Sold_outSerializers
    permission_classes = (AdminPermission,)

class Sold_outdetailapieview(generics.RetrieveAPIView):
    queryset = Sold_out.objects.all()
    serializer_class = Sold_outSerializers
    permission_classes = (AdminPermission,)
