# Generated by Django 2.0.4 on 2018-05-12 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ceremonia', '0002_auto_20180504_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='decoracionceremoniacarrito',
            name='subtotal',
            field=models.BigIntegerField(default=0),
        ),
    ]
