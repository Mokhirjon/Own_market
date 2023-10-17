from django.contrib import admin
from .models import Sold_out
# Register your models here.
class Sold_outAdmin(admin.ModelAdmin):
    list_display = ('sold_shoes','sold_clothes','sold_pants','sold_things')


admin.site.register(Sold_out,Sold_outAdmin)