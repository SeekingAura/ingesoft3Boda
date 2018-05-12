# Generated by Django 2.0.4 on 2018-05-10 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('precio', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AlimentoCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField(default=1)),
                ('Alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fiesta.Alimento')),
            ],
        ),
        migrations.CreateModel(
            name='DecoracionFiesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('imagen', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('precio', models.BigIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Decoración',
                'verbose_name_plural': 'Decoraciones',
            },
        ),
        migrations.CreateModel(
            name='DecoracionFiestaCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('Decoracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fiesta.DecoracionFiesta')),
            ],
        ),
        migrations.CreateModel(
            name='Entretenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('precio', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EntretenimientoCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entretenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fiesta.Entretenimiento')),
            ],
        ),
        migrations.CreateModel(
            name='FiestaEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fotos', models.BooleanField(default=False)),
                ('precio', models.BigIntegerField(default=0)),
                ('Boda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Domain.Boda')),
                ('Lugar', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Domain.Lugar')),
            ],
        ),
        migrations.AddField(
            model_name='entretenimientocarrito',
            name='FiestaEvento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fiesta.FiestaEvento'),
        ),
        migrations.AddField(
            model_name='decoracionfiestacarrito',
            name='FiestaEvento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fiesta.FiestaEvento'),
        ),
        migrations.AddField(
            model_name='alimentocarrito',
            name='FiestaEvento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fiesta.FiestaEvento'),
        ),
    ]
