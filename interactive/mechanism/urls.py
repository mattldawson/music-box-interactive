from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.molecules),
    path('molecules', views.molecules),
    path('reactions', views.reactions),
    path('load', views.load),
    path('edit', views.edit),
    path('equation', views.equation),
    path('save', views.save)
    ]
