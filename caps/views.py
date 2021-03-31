import pdb
from django.shortcuts import render
from django.utils.timezone import activate
from django.views.generic import View, CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .models import Season, Episodies
from social.models import Social
from .forms import SeasonForm, EpisodieForm


class SeasonView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            socials = Social.objects.all()
            season = Season.objects.get(slug=slug)
            episodies = Episodies.objects.filter(
                season__name=season.name).order_by('ordering')
        except:
            season = None
            episodies = None

        context = {
            "season": season,
            "episodies": episodies,
            "socials": socials,
        }

        return render(request, 'seasonlist.html', context)


class EpisodieView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            episodie = Episodies.objects.get(slug=slug)
            number_n = episodie.ordering + 1
            number_s = episodie.ordering - 1
            if number_s == 0:
                number_s = 1
            next_ep = Episodies.objects.get(ordering=number_n)
            prev_ep = Episodies.objects.get(ordering=number_s)
            socials = Social.objects.all()
        except:
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
        }
        return render(request, 'espisodie.html', context)


@method_decorator(login_required, name='dispatch')
class CreateSeasonView(CreateView):
    model = Season
    form_class = SeasonForm
    template_name = 'admin/season_form.html'
    success_url = reverse_lazy('administration')


@method_decorator(login_required, name='dispatch')
class SeasonUpdateView(UpdateView):
    model = Season
    form_class = SeasonForm
    template_name = 'admin/season_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('administration')
    """
    def get_success_url(self):
        return reverse_lazy('updateSeason', args=[self.object.id]) + '?ok'
    """


@method_decorator(login_required, name='dispatch')
class ListSeasonAdminView(ListView):
    model = Season
    template_name = 'admin/seasons_admin_list.html'
    context_object_name = 'seasons'


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
