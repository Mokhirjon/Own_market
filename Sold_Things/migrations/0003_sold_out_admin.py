# Generated by Django 4.2.3 on 2023-10-24 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Sold_Things', '0002_rename_sold_cpsh_sold_out_sold_things'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold_out',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
