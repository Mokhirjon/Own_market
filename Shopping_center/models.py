from django.db import models
from datetime import datetime
from account.models import Customuser
# Create your models here.
class Shopping_center(models.Model):
    shopping_center_name =  models.CharField(max_length=50,default='')
    Shoes_SH = models.CharField(max_length=50,default='')
    Clothes = models.CharField(max_length=60,default='')
    Pants = models.CharField(max_length=40,default='')

    def __str__(self):
        return self.shopping_center_name
    class Meta:
        db_table = 'Shopping_center'

class Shoes(models.Model):
    shoes = models.ForeignKey(Shopping_center,on_delete=models.CASCADE)
    shoes_name = models.CharField(max_length=45,default='')
    image = models.ImageField(upload_to='shoes_man/')
    price = models.CharField(max_length=45)
    brand = models.CharField(max_length=50)
    about_shoes = models.TextField()
    colour = models.CharField(max_length=35,default='')
    size = models.SmallIntegerField()
    year_created = models.DateField()
    made_in_from = models.CharField(max_length=30)
    if_sold = models.BooleanField(default=datetime.now)
    for_which_season = models.CharField(max_length=20,default='')
    Contact_with_admin = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.shoes_name
    class Meta:
        db_table = 'Shoes'




    

    