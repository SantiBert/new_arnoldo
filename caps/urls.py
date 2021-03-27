from django.contrib import admin
from django.urls import path
from .views import SeasonView, EpisodieView

caps_patterns = ([
    path('season/<str:slug>/', SeasonView.as_view(), name='season'),
    path('episodie/<slug:slug>/', EpisodieView.as_view(), name='episodieDetail'),
], 'caps')
