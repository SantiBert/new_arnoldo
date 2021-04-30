import pdb
from django.shortcuts import render
from django.utils.timezone import activate
from django.views.generic import View, CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Season, Episodies
from social.models import Social
from .forms import SeasonForm, EpisodieForm

# Vista para las Temporadas para el usuario


class SeasonView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            socials = Social.objects.all()
            season = Season.objects.get(slug=slug)
            episodies = Episodies.objects.filter(
                season__name=season.name).order_by('ordering')
            number_n = season.ordering + 1
            number_s = season.ordering - 1
            if number_s == 0:
                number_s = 1
            if number_n > 6:
                number_n = 6
            next_se = Season.objects.get(ordering=number_n)
            prev_se = Season.objects.get(ordering=number_s)

        except:
            socials = None
            season = None
            episodies = None
            number_n = None
            number_s = None
            next_se = None
            prev_se = None

        context = {
            "season": season,
            "episodies": episodies,
            "socials": socials,
            "next_se": next_se,
            "prev_se": prev_se,
        }

        return render(request, 'seasonlist.html', context)

# Vista para los episodios (filtrados por temporada) para el usuario


class EpisodieView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            episodie = Episodies.objects.get(slug=slug)
            season = episodie.season
            number_n = episodie.ordering + 1
            number_s = episodie.ordering - 1
            if number_s == 0:
                number_s = 1
            #numero limite de episodios para que funcione el next y prev
            if number_n > 103:
                number_n = 103
            next_ep = Episodies.objects.get(ordering=number_n)
            prev_ep = Episodies.objects.get(ordering=number_s)
            socials = Social.objects.all()
        except:
            season = None
            episodie = None
            number_n = None
            number_s = None
            next_ep = None
            prev_ep = None
            socials = None
        context = {
            "episodie": episodie,
            "next_ep": next_ep,
            "prev_ep": prev_ep,
            "socials": socials,
            "season": season
        }
        return render(request, 'espisodie.html', context)

# Vista para crear una temporada para el administrador
@method_decorator(login_required, name='dispatch')
class CreateSeasonView(CreateView):
    model = Season
    form_class = SeasonForm
    template_name = 'admin/season_form.html'
    success_url = reverse_lazy('administration')


# Vista para editar una temporada para el administrador
@method_decorator(login_required, name='dispatch')
class SeasonUpdateView(UpdateView):
    model = Season
    form_class = SeasonForm
    template_name = 'admin/season_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('admin_caps:listSeason')


@method_decorator(login_required, name='dispatch')
class ListSeasonAdminView(ListView):
    model = Season
    template_name = 'admin/seasons_admin_list.html'
    context_object_name = 'seasons'
    ordering = 'ordering'


@method_decorator(login_required, name='dispatch')
class CreateEpisodieView(CreateView):
    model = Episodies
    form_class = EpisodieForm
    template_name = 'admin/episodie_form.html'
    success_url = reverse_lazy('administration')


@method_decorator(login_required, name='dispatch')
class EpisodieUpdateView(UpdateView):
    model = Episodies
    form_class = EpisodieForm
    template_name = 'admin/episodie_update_form.html'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('admin_caps:updateEpisodie', args=[self.object.id]) + '?ok'


@method_decorator(login_required, name='dispatch')
class ListEpisodieAdminView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            season = Season.objects.get(slug=slug)
            episodies = Episodies.objects.filter(
                season__name=season.name).order_by('ordering')
        except:
            season = None
            episodies = None

        context = {
            "season": season,
            "episodies": episodies,
        }

        return render(request, 'admin/episodies_admin_list.html', context)


class SearchTagView(View):
    def get(self, request, tag, *args, **kwargs):
        queryset = tag
        socials = Social.objects.all()
        seasons = Season.objects.filter(is_active=True)
        if queryset:
            episodies = Episodies.objects.filter(
                tags__name__in=[tag], is_active=True).distinct().order_by('ordering')
        context = {
            "episodies": episodies,
            "tag": queryset,
        }

        return render(request, 'tagresult.html', context)
