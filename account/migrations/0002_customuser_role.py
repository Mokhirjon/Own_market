# Generated by Django 4.2.5 on 2023-09-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'admin'), (2, 'writter'), (3, 'reader')], default=1),
        ),
    ]