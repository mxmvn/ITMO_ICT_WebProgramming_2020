# Generated by Django 3.0.4 on 2020-03-21 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_make', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_color', models.CharField(max_length=50)),
                ('id_car', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Car_owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=50)),
                ('owner_surname', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Owning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_start_owning', models.DateField()),
                ('date_of_end_owning', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car_owner')),
            ],
        ),
        migrations.CreateModel(
            name='Driver_license',
            fields=[
                ('id_license', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_of_issue', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car_owner')),
            ],
        ),
    ]
