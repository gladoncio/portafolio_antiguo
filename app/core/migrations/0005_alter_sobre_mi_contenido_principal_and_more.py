# Generated by Django 4.1.5 on 2023-01-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_sobre_mi_contenido_principal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobre_mi',
            name='contenido_principal',
            field=models.CharField(max_length=400, verbose_name='contenido'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='cuatro',
            field=models.CharField(max_length=400, verbose_name='contenido 4'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='dos',
            field=models.CharField(max_length=400, verbose_name='contenido 2'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='tercer_contenido',
            field=models.CharField(max_length=400, verbose_name='tercer contenido'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='titulo_cuatro',
            field=models.CharField(max_length=400, verbose_name='titulo 4'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='titulo_dos',
            field=models.CharField(max_length=400, verbose_name='titulo 2'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='titulo_tres',
            field=models.CharField(max_length=400, verbose_name='titulo 3'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='titulo_uno',
            field=models.CharField(max_length=400, verbose_name='titulo 1'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='tres',
            field=models.CharField(max_length=400, verbose_name='contenido 3'),
        ),
        migrations.AlterField(
            model_name='sobre_mi',
            name='uno',
            field=models.CharField(max_length=400, verbose_name='contenido 1'),
        ),
    ]
