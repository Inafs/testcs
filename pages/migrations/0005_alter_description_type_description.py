# Generated by Django 4.0.6 on 2022-07-21 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_description_type_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='type_description',
            field=models.CharField(choices=[('Заголовок', 'Заголовок'), ('Текст', 'Текст')], default='Заголовок', max_length=9, verbose_name='Тип Описания'),
        ),
    ]