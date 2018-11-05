# Generated by Django 2.1.3 on 2018-11-02 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('nit', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('correo', models.CharField(max_length=60)),
                ('fecha_de_rentacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renta.Cliente')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Renta.Equipo')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='equipos',
            field=models.ManyToManyField(through='Renta.Rentacion', to='Renta.Equipo'),
        ),
    ]
