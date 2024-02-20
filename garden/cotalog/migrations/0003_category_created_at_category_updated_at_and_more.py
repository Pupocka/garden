# Generated by Django 5.0.2 on 2024-02-20 18:38

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotalog', '0002_alter_category_options_alter_plant_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время первичного создания сущности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Время последнего обновление сущности'),
        ),
        migrations.AddField(
            model_name='plant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время первичного создания сущности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plant',
            name='description',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='plant',
            name='mesurement_unit',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Единица измерения (шт, грамм, кг и тп...)'),
        ),
        migrations.AddField(
            model_name='plant',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='plant',
            name='slag',
            field=models.SlugField(default=datetime.datetime(2024, 2, 20, 18, 38, 51, 993649, tzinfo=datetime.timezone.utc), verbose_name='слаг (название транслитом)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plant',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Время последнего обновление сущности'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Фотография категории'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='cotalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='PlantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время первичного создания сущности')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего обновление сущности')),
                ('image', models.ImageField(upload_to='media', verbose_name='Фотография растения')),
                ('undertitle', models.CharField(blank=True, max_length=256, null=True, verbose_name='Подпись фотографии')),
                ('plant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plantimages', to='cotalog.plant', verbose_name='Растения')),
            ],
            options={
                'verbose_name': 'Фотография растения.',
                'verbose_name_plural': 'Фотографии растения.',
            },
        ),
    ]
