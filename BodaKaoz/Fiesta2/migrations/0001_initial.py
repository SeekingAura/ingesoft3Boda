# Generated by Django 2.0.2 on 2018-02-26 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Domain', '0001_initial'),
        ('Ceremonia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecoracionFiestaCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('Decoracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Domain.Decoracion')),
                ('FiestaEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ceremonia.CeremoniaEvento')),
            ],
        ),
        migrations.CreateModel(
            name='Entretenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(default=None, null=True, upload_to='')),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EntretenimientoCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entretenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fiesta2.Entretenimiento')),
                ('FiestaEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ceremonia.CeremoniaEvento')),
            ],
        ),
    ]
