from django import forms
from Pants.models import Pants
from Shopping_center.models import Shoes
from Clothes.models import Clothes



class PantsForm(forms.ModelForm):
    pants_colour_uz = forms.CharField()
    pants_colour_ru = forms.CharField(required=False)
    pants_colour_en = forms.CharField(required=False)

    about_pants_uz = forms.CharField()
    about_pants_ru = forms.CharField(required=False)
    about_pants_en = forms.CharField(required=False)

    class Meta:
        model = Pants
        exclude = ('pants_colour',' about_pants')

class ShoesForm(forms.ModelForm):
    colour_uz = forms.CharField()
    colour_ru = forms.CharField(required=False)
    colour_en = forms.CharField(required=False)

    about_shoes_uz = forms.CharField()
    about_shoes_ru = forms.CharField(required=False)
    about_shoes_en = forms.CharField(required=False)

    class Meta:
        model = Shoes
        exclude = ('colour',' about_shoes')

class ClothesForm(forms.ModelForm):
    clothes_colour_uz = forms.CharField()
    clothes_colour_ru = forms.CharField(required=False)
    clothes_colour_en = forms.CharField(required=False)

    about_clothes_uz = forms.CharField()
    about_clothes_ru = forms.CharField(required=False)
    about_clothes_en = forms.CharField(required=False)

    class Meta:
        model = Shoes
        exclude = ('clothes_colour',' about_clothes')