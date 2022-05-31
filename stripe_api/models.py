from django.db import models


class Item(models.Model):
    name = models.CharField(
        'название товара',
        db_index=True,
        max_length=500
    )
    description = models.TextField('опсиание')
    price = models.DecimalField(
        'цена',
        max_digits=6,
        decimal_places=2
    )
