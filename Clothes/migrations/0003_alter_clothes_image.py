# Generated by Django 4.2.5 on 2023-09-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothes', '0002_rename_about_shoes_clothes_about_clothes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(upload_to='clothes_man/'),
        ),
    ]
