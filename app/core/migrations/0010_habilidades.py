# Generated by Django 4.1.5 on 2023-01-28 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_header_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('titulo', models.CharField(max_length=140, verbose_name='titulo')),
                ('contenido', models.CharField(max_length=500, verbose_name='contenido')),
            ],
        ),
    ]