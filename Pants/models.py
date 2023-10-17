from django.db import models
from Shopping_center.models import Shopping_center
from datetime import datetime
from account.models import Customuser
# Create your models here.
class Pants(models.Model):
    pants = models.ForeignKey(Shopping_center,on_delete=models.CASCADE)
    pants_name = models.CharField(max_length=25,default='')
    image = models.ImageField(upload_to='pants_man/')
    pants_price = models.CharField(max_length=45)
    pants_brand = models.CharField(max_length=50)
    about_pants = models.TextField()
    pants_colour = models.CharField(max_length=35, default='')
    pants_size = models.SmallIntegerField()
    pants_year_created = models.DateField()
    pants_made_in_from = models.CharField(max_length=30)
    if_sold = models.BooleanField(default=datetime.now)
    pants_for_which_season = models.CharField(max_length=20, default='')
    Contact_with_admin = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.pants_name
    class Meta:
        db_table = 'Pants'