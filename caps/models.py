
from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone


class Season(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to='Season/', default='default/logoarnoldo.png' ,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Episodies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    season = models.ForeignKey(
        Season, on_delete=models.PROTECT)    
    ordering = models.PositiveSmallIntegerField('Número de capitulo',default=0)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Episodie/',default='default/logoarnoldo.png', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Links(models.Model):
    id = models.AutoField(primary_key=True)
    enlase = models.URLField(max_length=150, null=True, blank=True)
    episodie = models.ForeignKey(
        Episodies, related_name="episodie", on_delete=models.PROTECT)
    spanish = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
