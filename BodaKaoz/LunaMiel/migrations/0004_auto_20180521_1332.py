# Generated by Django 2.0.4 on 2018-05-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LunaMiel', '0003_auto_20180519_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='imagen',
            field=models.ImageField(default='', upload_to='LunaMiel/Actividad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='imagen',
            field=models.ImageField(default='', upload_to='LunaMiel/Hotel'),
            preserve_default=False,
        ),
    ]
