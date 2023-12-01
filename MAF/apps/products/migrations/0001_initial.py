

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категории')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, verbose_name='Подкатегории')),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('compound', models.TextField(verbose_name='Состав')),
                ('description', models.TextField(verbose_name='Описание')),
                ('applying', models.TextField(verbose_name='Применение')),
                ('waiting_time', models.TextField(verbose_name='Время ожидания')),
                ('release_form', models.TextField(verbose_name='Форма выпуска')),
                ('storage_date', models.TextField(verbose_name='Срок хранение')),
                ('storage_conditions', models.TextField(verbose_name='Условия хранения ')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.subcategory')),
            ],
            options={
                'verbose_name': 'Препарат',
                'verbose_name_plural': 'Препараты',
            },
        ),
    ]
