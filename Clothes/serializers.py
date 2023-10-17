from rest_framework import serializers
from .models import Clothes

class ClothesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ("shoes", 'image', 'price', 'brand', 'about_shoes', 'colour', 'size', 'year_created', 'made_in_from',
                  'if_sold', 'for_which_season', 'Contact_with_admin')