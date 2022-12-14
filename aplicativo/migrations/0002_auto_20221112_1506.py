# Generated by Django 3.2.16 on 2022-11-12 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='data_compra',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='banco',
            name='numero',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Número de Bilhetes'),
        ),
        migrations.AlterField(
            model_name='banco',
            name='recarga',
            field=models.IntegerField(help_text='Insira valor da Recarga', max_length=100, null=True, verbose_name='Recarga'),
        ),
        migrations.AlterField(
            model_name='banco',
            name='saldo',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Saldo'),
        ),
    ]
