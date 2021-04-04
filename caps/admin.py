from django.contrib import admin
from .models import Season, Episodies
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SeasonResourseces(resources.ModelResource):
    class Meta:
        model = Season


class EpisodiesResourseces(resources.ModelResource):
    class Meta:
        model = Episodies


class SeasonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ['name']
    resource_class = SeasonResourseces


class EpisodiesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ['name']
    resource_class = EpisodiesResourseces


admin.site.register(Season, SeasonAdmin)
admin.site.register(Episodies, EpisodiesAdmin)
