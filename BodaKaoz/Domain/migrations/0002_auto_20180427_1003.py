# Generated by Django 2.0.4 on 2018-04-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Domain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='tipo',
            field=models.CharField(blank=True, choices=[('ceremonia', 'Ceremonia'), ('fiesta', 'Fiesta')], default=None, max_length=50, null=True),
        ),
    ]