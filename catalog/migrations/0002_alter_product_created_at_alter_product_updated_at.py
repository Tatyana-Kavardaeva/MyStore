# Generated by Django 5.0.7 on 2024-07-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                help_text='Дата и время создания продукта',
                null=True,
                verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True,
                help_text='Дата и время последнего обновления продукта',
                null=True,
                verbose_name='Дата обновления'),
        ),
    ]