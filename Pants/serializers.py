from rest_framework import serializers
from .models import Pants

class PantsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pants
        fields = ("shoes", 'image', 'price', 'brand', 'about_shoes', 'colour', 'size', 'year_created', 'made_in_from',
                  'if_sold', 'for_which_season', 'Contact_with_admin')