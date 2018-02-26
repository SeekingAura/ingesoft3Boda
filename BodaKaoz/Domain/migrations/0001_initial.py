# Generated by Django 2.0.2 on 2018-02-26 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pareja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(default=0)),
                ('Enamorado1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Enamorado1', to='Pareja.Enamorado')),
                ('Enamorado2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Enamorado2', to='Pareja.Enamorado')),
            ],
        ),
        migrations.CreateModel(
            name='Decoracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=50, null=True)),
                ('descripcion', models.CharField(default=None, max_length=50, null=True)),
                ('imagen', models.ImageField(default=None, null=True, upload_to='')),
                ('precio', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Decoración',
                'verbose_name_plural': 'Decoraciones',
            },
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=50, null=True)),
                ('descripcion', models.CharField(default=None, max_length=50, null=True)),
                ('tipo', models.CharField(default=None, max_length=50, null=True)),
                ('imagen', models.ImageField(default=None, null=True, upload_to='')),
                ('precio', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Fotos',
                'verbose_name_plural': 'Fotos',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField()),
                ('imagen', models.ImageField(default=None, null=True, upload_to='')),
                ('precio', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TransporteCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Boda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Domain.Boda')),
                ('Transporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Domain.Transporte')),
            ],
        ),
    ]
