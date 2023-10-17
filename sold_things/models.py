from django.db import models
# Create your models here.

class Sold_out (models.Model):
    sold_things = models.CharField(max_length=24,default='')
    sold_clothes = models.TextField()
    sold_pants= models.TextField()
    sold_shoes = models.TextField()

    def __str__(self):
        return self.sold_things
    class Meta:
        db_table : 'Sold_out'
