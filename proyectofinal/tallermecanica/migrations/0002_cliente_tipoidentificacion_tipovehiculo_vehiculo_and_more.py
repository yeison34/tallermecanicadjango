# Generated by Django 4.1.6 on 2023-03-01 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallermecanica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=300)),
                ('apellido', models.CharField(max_length=300)),
                ('telefono', models.CharField(max_length=12)),
                ('correo', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
                ('idciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tallermecanica.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='tipoidentificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='tipovehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=100)),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tallermecanica.cliente')),
                ('idciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tallermecanica.ciudad')),
                ('idtipovehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tallermecanica.tipovehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='idtipoidentificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tallermecanica.tipoidentificacion'),
        ),
    ]
