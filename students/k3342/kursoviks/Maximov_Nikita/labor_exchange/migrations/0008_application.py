# Generated by Django 3.0 on 2020-10-06 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labor_exchange', '0007_delete_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Одобрена', 'Одобрена'), ('В_процесе', 'В Процесе'), ('Отклонена', 'Отклонена')], max_length=20, verbose_name='Статус')),
                ('date', models.DateField(verbose_name='Дата подачи')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labor_exchange.Resume')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labor_exchange.Vacancy')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
