from django.contrib import admin
from .models import Clothes
# Register your models here.
class ClothesAdmin(admin.ModelAdmin):
    list_display = ("clothes", 'image', 'clothes_price', 'clothes_brand', 'about_clothes',
                    'clothes_colour', 'clothes_size', 'clothes_year_created', 'clothes_made_in_from',
                  'if_sold', 'clothes_for_which_season', 'Contact_with_admin')
    search_fields = ["clothes",'clothes_size','clothes_made_in_from', 'clothes_for_which_season','clothes_brand']
admin.site.register(Clothes,ClothesAdmin)