# Generated by Django 3.0.7 on 2020-06-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_auto_20200630_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
    ]
