from django.contrib import admin
from .models import Social
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SocialResourseces(resources.ModelResource):
    class Meta:
        model = Social


class SocialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ['name']
    resource_class = SocialResourseces


admin.site.register(Social)
