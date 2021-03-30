
from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
from django.conf import settings


def get_upload_caps_path(instance, filename):
    return '/'.join([settings.FILES_PATH, "caps", str(instance.caps.id), filename])


class Season(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(
        upload_to='Season/', default='logoarnoldo.png', null=True, blank=True)
    banner = models.ImageField(upload_to='Season/', null=True, blank=True)
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
    ordering = models.PositiveSmallIntegerField(
        'Número de capitulo', default=0)
    description = models.TextField(null=True, blank=True)
    link1 = models.URLField('Link 1', max_length=1300, null=True, blank=True)
    link2 = models.URLField('Link 2', max_length=1300, null=True, blank=True)
    english = models.URLField(
        'English', max_length=1300, null=True, blank=True)
    spoty = models.URLField('Spotify', max_length=1300, null=True, blank=True)
    mediafire = models.URLField(
        'Mediafire', max_length=1300, null=True, blank=True)
    image = models.ImageField(
        upload_to='Episodie/', default='logoarnoldo.png', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
