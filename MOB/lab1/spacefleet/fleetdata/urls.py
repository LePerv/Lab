from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('race/', views.race, name='race'),
    path('pilot/', views.pilot, name='pilot'),
    path('starship/', views.starship, name='starship'),
    path('station/', views.station, name='station'),
    path('fleet/', views.fleet, name='fleet'),
]