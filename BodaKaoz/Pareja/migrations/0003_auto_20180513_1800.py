# Generated by Django 2.0.4 on 2018-05-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pareja', '0002_auto_20180513_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='belleza',
            name='maquillaje',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='belleza',
            name='peinado',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='prenda',
            name='descripcion',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='prenda',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]
