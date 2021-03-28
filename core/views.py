from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from caps.models import Season, Episodies
from social.models import Social


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seasons'] = Season.objects.filter(is_active=True)
        context['socials'] = Social.objects.all()
        return context


class SearchView(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        socials = Social.objects.all()
        seasons = Season.objects.filter(is_active=True)
        if queryset:
            episodies = Episodies.objects.filter(
                Q(name__icontains=queryset) |
                Q(description__icontains=queryset),
                is_active=True
            ).distinct().order_by('ordering')
        context = {
            "socials": socials,
            "seasons": seasons,
            "episodies": episodies,
        }
        return render(request, 'results.html', context)


@method_decorator(login_required, name='dispatch')
class AdministrationView(TemplateView):
    template_name = 'administration.html'


@method_decorator(login_required, name='dispatch')
class SearchAdminView(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        if queryset:
            episodies = Episodies.objects.filter(
                Q(name__icontains=queryset) |
                Q(description__icontains=queryset),
                is_active=True
            ).distinct().order_by('ordering')
        context = {
            "episodies": episodies,
        }
        return render(request, 'admin_results.html', context)
