# Generated by Django 2.0.2 on 2018-02-26 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LunaMiel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'verbose_name': 'Actividad', 'verbose_name_plural': 'Actividades'},
        ),
        migrations.AlterModelOptions(
            name='actividadplan',
            options={'verbose_name': 'Actividad plan', 'verbose_name_plural': 'Actividad planes'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name': 'Hotel', 'verbose_name_plural': 'Hoteles'},
        ),
        migrations.AlterModelOptions(
            name='hotelplan',
            options={'verbose_name': 'Hotel plan', 'verbose_name_plural': 'Hotel planes'},
        ),
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': 'Plan', 'verbose_name_plural': 'Planes'},
        ),
    ]
