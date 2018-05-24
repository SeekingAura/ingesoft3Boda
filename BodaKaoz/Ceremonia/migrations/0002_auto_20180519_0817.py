# Generated by Django 2.0.4 on 2018-05-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ceremonia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decoracionceremonia',
            name='descripcion',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ministro',
            name='imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='Ceremonia/Ministro'),
        ),
        migrations.AlterField(
            model_name='ministro',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='musica',
            name='descripcion',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='musica',
            name='imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='Ceremonia/Musica'),
        ),
        migrations.AlterField(
            model_name='musica',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]