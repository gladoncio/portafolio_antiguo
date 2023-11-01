# Generated by Django 4.1.5 on 2023-01-31 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faltante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('ver_video', models.CharField(max_length=140, verbose_name='video')),
                ('volver', models.CharField(max_length=140, verbose_name='back')),
                ('diseno', models.CharField(max_length=140, verbose_name='diseño')),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('idioma', models.CharField(max_length=140, verbose_name='idioma')),
            ],
        ),
    ]
