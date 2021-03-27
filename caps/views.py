from django.shortcuts import render
from django.utils.timezone import activate
from django.views.generic import View, DetailView

from .models import Season, Episodies, Links


class SeasonView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            season = Season.objects.get(slug=slug)
            episodies = Episodies.objects.filter(season__name=season.name)
        except:
            season = None
            episodies = None

        context = {
            "season": season,
            "episodies": episodies,
        }

        return render(request, 'seasonlist.html', context)


class EpisodieView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            episodie = Episodies.objects.get(slug=slug)
            spanish = Links.objects.filter(episodie=episodie, spanish=True)
            english = Links.objects.filter(episodie=episodie, spanish=False)
            link1 = spanish[0]
            link2 = spanish[1]
            link3 = english[0]

        except:
            episodie = None
            spanish = None
            english = None
            link1 = None
            link2 = None
            link3 = None

        context = {
            "episodie": episodie,
            "spanish": spanish,
            "link1": link1,
            "link2": link2,
            "link3": link3,
        }
        return render(request, 'espisodie.html', context)
