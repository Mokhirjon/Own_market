from rest_framework import serializers
from .models import Shoes,Shopping_center

class Shopping_centerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shopping_center
        fields = (" shopping_center_name",'Shoes_SH','Clothes','Pants')
class ShoesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = ("shoes",'image','price','brand','about_shoes','colour','size','year_created','made_in_from',
                  'if_sold','for_which_season','Contact_with_admin')



