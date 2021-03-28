from django.contrib import admin
from django.urls import path
from .views import IndexView, AdministrationView, SearchView, SearchAdminView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('results', SearchView.as_view(), name='search'),
    path('administration/', AdministrationView.as_view(), name='administration'),
    path('adminstration/result', SearchAdminView.as_view(), name='adminSearch'),
]
