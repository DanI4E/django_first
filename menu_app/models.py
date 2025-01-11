from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Menu(models.Model):
    objects = None
    menu_label = models.CharField(max_length=256, blank=True, null=False)

    def __str__(self):
        return f'{self.id}: {self.menu_label}'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, blank=False, null=False, related_name='links')
    title = models.CharField(max_length=32, blank=True, null=False)
    url = models.CharField(max_length=256, blank=True, null=False)
    icon = models.ImageField(max_length=32, blank=True, null=False)
    priority = models.SmallIntegerField(validators=[MinValueValidator(-100), MaxValueValidator(100)], default=0)

    def __str__(self):
        return f'{self.id}: {self.title}'
