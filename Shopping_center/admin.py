from django.contrib import admin
from .models import Shopping_center,Shoes
from config.forms import ShoesForm
# Register your models here.
class ShoesAdmin(admin.ModelAdmin):
    form = ShoesForm
    list_display = ("shoes", 'image', 'price', 'brand', 'about_shoes',
                    'colour', 'size', 'year_created', 'made_in_from',
                  'if_sold', 'for_which_season', 'Contact_with_admin')
    search_fields = ["shoes",'size','made_in_from', 'for_which_season','brand']
class ShoppingcenterAdmin(admin.ModelAdmin):
    list_display = ('shopping_center_name','Shoes_SH','Clothes','Pants')
    search_fields = ['Shoes_SH','Clothes','Pants']



admin.site.register(Shoes,ShoesAdmin)
admin.site.register(Shopping_center,ShoppingcenterAdmin)