# Generated by Django 3.0.7 on 2020-06-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='hotel_owner',
            field=models.CharField(max_length=100, verbose_name='Имя владельца'),
        ),
    ]
