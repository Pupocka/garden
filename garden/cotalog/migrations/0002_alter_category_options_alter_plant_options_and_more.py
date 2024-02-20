# Generated by Django 5.0.2 on 2024-02-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='plant',
            options={'verbose_name': 'Растение', 'verbose_name_plural': 'Растения'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Фотография категории'),
        ),
    ]