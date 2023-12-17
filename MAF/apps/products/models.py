from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Категории', max_length=150)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(verbose_name="Подкатегории", max_length=130)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    compound = models.TextField(verbose_name='Состав')
    description = models.TextField(verbose_name='Описание')
    applying = models.TextField(verbose_name='Применение')
    waiting_time = models.TextField(verbose_name='Период ожидания')
    release_form = models.TextField(verbose_name='Форма выпуска')
    storage_date = models.TextField(verbose_name='Состав')
    storage_conditions = models.TextField(verbose_name='Срок хранения')
    # category = models.ForeignKey(Category,null=True,blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, verbose_name='Какой подкатегории относится?')

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255, null=False)
    phone = models.IntegerField(verbose_name='Телефон', null=False)
    email = models.EmailField(verbose_name='email', null=True)
    date = models.DateTimeField('Дата создания заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-date']

    def __str__(self):
        return f'Имя {self.name}, Номер телефона {self.phone}, email {self.email}'

