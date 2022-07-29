from django.utils import timezone
from django.db import models
from datetime import datetime


class PaletteSauron(models.Model):
    class Type(models.TextChoices):
        indus = 'Industrielle'
        auto = 'Auto standard'
        auto_agm = 'Auto AGM'
        moto_wet = 'Moto Wet'

    reference = models.CharField(max_length=20)
    date_code = models.CharField(max_length=20)
    dateTransfert = models.DateField(default=timezone.now)
    voltage = models.FloatField(default=12.40)
    number_of_palettes = models.IntegerField(default=1)
    quantity_per_palette = models.IntegerField()
    type = models.fields.CharField(choices=Type.choices, max_length=20)

    date_limite = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.reference}'


class PalettePicard(models.Model):
    class Type(models.TextChoices):
        indus = 'Industrielle'
        auto = 'Auto standard'
        auto_agm = 'Auto AGM'
        moto_wet = 'Moto Wet'

    reference = models.CharField(max_length=20)
    date_code = models.CharField(max_length=20)
    dateTransfert = models.DateField(default=timezone.now)
    voltage = models.FloatField(default=12.40)
    number_of_palettes = models.IntegerField(default=1)
    quantity_per_palette = models.IntegerField()
    type = models.fields.CharField(choices=Type.choices, max_length=20)

    date_limite = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.reference}'