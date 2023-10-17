from rest_framework import serializers
from .models import Sold_out

class Sold_outSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sold_out
        fields = ('sold_shoes','sold_clothes','sold_pants','sold_things')