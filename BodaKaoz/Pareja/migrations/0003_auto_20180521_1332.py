# Generated by Django 2.0.4 on 2018-05-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pareja', '0002_auto_20180519_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio',
            name='imagen',
            field=models.ImageField(default='', upload_to='Pareja/Accesorio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='belleza',
            name='imagen',
            field=models.ImageField(default='', upload_to='Pareja/Belleza'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prenda',
            name='imagen',
            field=models.ImageField(default='', upload_to='Pareja/Prenda'),
            preserve_default=False,
        ),
    ]
