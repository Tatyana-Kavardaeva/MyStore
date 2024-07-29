from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Введите название категории',
                            verbose_name='Название')
    description = models.TextField(blank=True,
                                   null=True,
                                   help_text='Введите описание категории',
                                   verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Введите наименование продукта',
        verbose_name='Наименование'
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text='Введите описание продукта',
        verbose_name='Описание')

    image = models.ImageField(
        upload_to="products/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
        related_name='catalog'
    )
    price = models.IntegerField(
        verbose_name="Стоимость продукта",
        default=0,
        help_text="Введите целое стоимость"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания продукта",
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        help_text="Дата и время последнего обновления продукта",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ["category", "name", "price", "created_at", "updated_at"]
