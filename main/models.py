from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True} #Для необязательных полей


class Product(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Название продукта',
                                  help_text='Введите название продукта')
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, verbose_name='Название категории',
                                  help_text='Укажите название категории', related_name="products", **NULLABLE)
    avatar = models.ImageField(upload_to='products/', verbose_name='Аватвр',
                               help_text='Загрузите фото продукта', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Есть в продаже')
    date_born = models.DateField(verbose_name='Дата публикации', help_text='Укажите дату публикации продукта',
                                 **NULLABLE)

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('first_name', 'category',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории',
                            help_text='Введите название категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
