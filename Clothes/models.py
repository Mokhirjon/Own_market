from django.db import models
from Shopping_center.models import Shopping_center
from datetime import datetime
from account.models import Customuser
# Create your models here.
class Clothes(models.Model):
    clothes = models.ForeignKey(Shopping_center,on_delete=models.CASCADE)
    clothes_name = models.CharField(max_length=45,default='')
    image = models.ImageField(upload_to='clothes_man/')
    clothes_price = models.CharField(max_length=45)
    clothes_brand = models.CharField(max_length=50)
    about_clothes = models.TextField()
    clothes_colour = models.CharField(max_length=35, default='')
    clothes_size = models.SmallIntegerField()
    clothes_year_created = models.DateField()
    clothes_made_in_from = models.CharField(max_length=30)
    if_sold = models.BooleanField(default=datetime.now)
    clothes_for_which_season = models.CharField(max_length=20, default='')
    Contact_with_admin = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.clothes_name
    class Meta:
        db_table = 'Clothes'