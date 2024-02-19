from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название категории')
    image = models.ImageField(upload_to='media', verbose_name='Фотография категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Plant(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название растения')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории растений')

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def __str__(self) -> str:
        return self.title
