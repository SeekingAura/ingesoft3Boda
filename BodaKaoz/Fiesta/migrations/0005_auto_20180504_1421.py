# Generated by Django 2.0.4 on 2018-05-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fiesta', '0004_auto_20180427_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='precio',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='decoracionfiesta',
            name='precio',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entretenimiento',
            name='precio',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fiestaevento',
            name='Fotos',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fiestaevento',
            name='precio',
            field=models.BigIntegerField(default=0),
        ),
    ]