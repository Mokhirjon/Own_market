from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Customuser(AbstractUser):
    ROLE_CHOICES=(
        (1,'admin'),
        (2,'buyer')

    )
    role = models.SmallIntegerField(default=1,choices=ROLE_CHOICES)
    phone = models.CharField(default='',max_length=20)


