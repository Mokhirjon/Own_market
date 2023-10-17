from django.contrib import admin
from .models import Pants
# Register your models here.
class PantsAdmin(admin.ModelAdmin):
    list_display = ("pants", 'image', 'pants_price', 'pants_brand', 'about_pants',
                    'pants_colour', 'pants_size', 'pants_year_created', 'pants_made_in_from',
                  'if_sold', 'pants_for_which_season', 'Contact_with_admin')
    search_fields = ["pants",'size','pants_made_in_from', 'pants_for_which_season','pants_brand']
admin.site.register(Pants,PantsAdmin)