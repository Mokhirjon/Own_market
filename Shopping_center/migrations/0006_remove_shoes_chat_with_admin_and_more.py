# Generated by Django 4.2.5 on 2023-09-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping_center', '0005_shoes_shoes_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoes',
            name='Chat_with_admin',
        ),
        migrations.AddField(
            model_name='shoes',
            name='Contact_with_admin',
            field=models.CharField(default='', max_length=20),
        ),
    ]
