# Generated by Django 3.0.7 on 2020-06-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_auto_20200630_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='image',
            field=models.ImageField(upload_to='static/images', verbose_name='Изображение'),
        ),
    ]
