from modeltranslation.translator import translator,TranslationOptions
from Clothes.models import Clothes
from Pants.models import Pants
from Shopping_center.models import Shoes


class ShoesTranslation(TranslationOptions):
    fields = ('colour',' about_shoes')
class ClothesTranslation(TranslationOptions):
    fields = ('clothes_colour', ' about_clothes')

class PantsTranslation(TranslationOptions):
    fields =('pants_colour', ' about_pants')



translator.register(Shoes, ShoesTranslation)
translator.register(Clothes, ClothesTranslation)
translator.register(Pants, PantsTranslation)
