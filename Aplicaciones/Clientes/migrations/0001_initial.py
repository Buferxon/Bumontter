# Generated by Django 3.0.7 on 2023-04-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.BigIntegerField()),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Telefono', models.BigIntegerField()),
                ('Direccion', models.CharField(max_length=30)),
                ('Fecha_Registro', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
