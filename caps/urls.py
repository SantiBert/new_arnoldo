from django.contrib import admin
from django.urls import path
from .views import (SeasonView,
                    EpisodieView,
                    CreateEpisodieView,
                    CreateSeasonView,
                    ListSeasonAdminView,
                    ListEpisodieAdminView,
                    SeasonUpdateView,
                    EpisodieUpdateView,
                    )

caps_patterns = ([
    path('season/<str:slug>/', SeasonView.as_view(), name='season'),
    path('episodie/<slug:slug>/', EpisodieView.as_view(), name='episodieDetail'),
], 'caps')

caps_admin_patterns = ([
    path('episodie/create/', CreateEpisodieView.as_view(), name='createEpisodie'),
    path('season/create/', CreateSeasonView.as_view(), name='createSeason'),
    path('season/list/', ListSeasonAdminView.as_view(), name='listSeason'),
    path('<str:slug>/list/', ListEpisodieAdminView.as_view(), name='listEpisodies'),
    path('season/update/<slug:slug>/',
         SeasonUpdateView.as_view(), name='updateSeason'),
    path('episodie/update/<int:pk>/',
         EpisodieUpdateView.as_view(), name='updateEpisodie')
], 'admin_caps')
