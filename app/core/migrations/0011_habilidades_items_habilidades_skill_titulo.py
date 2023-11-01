# Generated by Django 4.1.5 on 2023-01-28 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_habilidades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades_items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('lenguaje', models.CharField(max_length=140, verbose_name='lenguaje')),
                ('porcentaje', models.CharField(max_length=50, verbose_name='porcentaje')),
            ],
        ),
        migrations.AddField(
            model_name='habilidades',
            name='skill_titulo',
            field=models.CharField(max_length=500, null=True, verbose_name='titulo_contenido'),
        ),
    ]