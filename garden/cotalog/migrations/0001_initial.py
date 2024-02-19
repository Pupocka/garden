# Generated by Django 5.0.2 on 2024-02-19 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название категории')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография категории')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название растения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotalog.category', verbose_name='Категории растений')),
            ],
        ),
    ]
