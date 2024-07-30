# Generated by Django 5.0.7 on 2024-07-30 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=0, help_text='Введите категорию продукта', on_delete=django.db.models.deletion.PROTECT, related_name='catalog', to='catalog.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата и время создания продукта', verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(help_text='Введите стоимость', verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления продукта', verbose_name='Дата обновления'),
        ),
    ]
