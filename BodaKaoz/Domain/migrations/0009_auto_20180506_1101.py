# Generated by Django 2.0.4 on 2018-05-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Domain', '0008_auto_20180506_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='tipo',
            field=models.CharField(choices=[('ceremonia', 'Ceremonia'), ('fiesta', 'Fiesta')], default=None, max_length=50),
        ),
    ]
