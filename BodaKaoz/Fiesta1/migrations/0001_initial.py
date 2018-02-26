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
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(default=None, null=True, upload_to='')),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AlimentoCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fiesta1.Alimento')),
                ('FiestaEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ceremonia.CeremoniaEvento')),
            ],
        ),
        migrations.CreateModel(
            name='FiestaEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(default=0)),
                ('Boda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Domain.Boda')),
                ('Fotos', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Domain.Fotos')),
                ('Lugar', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Domain.Lugar')),
            ],
        ),
    ]
