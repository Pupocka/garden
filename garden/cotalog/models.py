from django.db import models
from slugify import slugify


class TimeModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Время первичного создания сущности',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Время последнего обновление сущности',
        auto_now=True,
    )

    class Meta:
        abstract = True


class Category(TimeModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название категории',
    )
    image = models.ImageField(
        upload_to='media',
        verbose_name='Фотография категории',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return f'Категория - {self.title}; Список разновидностей {
            [variety.title for variety in Variety.objects.filter(
                category=self.pk
            )[:5]]
        }'


class Variety(TimeModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название вида растения (Лилия, Георгины, Гладиолус)',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='varieries',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Разновидность растения'
        verbose_name_plural = 'Разновидности растений'

    def __str__(self) -> str:
        return f'Разновидность - {self.title}; Список растений {
            [plant.title for plant in Plant.objects.filter(
                variety=self.pk
            )[:5]]
        }'


class Plant(TimeModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    description = models.CharField(
        max_length=512,
        verbose_name='Описание',
        blank=True,
        null=True,
    )
    price = models.FloatField(
        verbose_name='Цена',
        blank=True,
        null=True,
    )
    variety = models.ForeignKey(
        Variety,
        on_delete=models.CASCADE,
        verbose_name='Разновидность',
        related_name='plants',
        blank=True,
        null=True,
    )
    mesurement_unit = models.CharField(
        max_length=10,
        verbose_name='Единица измерения (шт, грамм, кг и тп...)',
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        verbose_name='слаг (название транслитом)',
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Plant, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Название: {self.title}, Разновидность: {self.variety.title}'


class Image(TimeModel):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='media',

        )
    undertitle = models.CharField(
        max_length=256,
        verbose_name='Подпись фотографии',
        blank=True,
        null=True,
    )
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        verbose_name='Растения',
        related_name='images',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Фотография растения'
        verbose_name_plural = 'Фотографии растения'

    def __str__(self) -> str:
        return (f'Растение: {self.plant.title}; '
                f'Описание: {self.undertitle[:15]}')
