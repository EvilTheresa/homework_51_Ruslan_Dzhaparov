from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_cat/', views.create_cat, name='create_cat'),
    path('cat_stats/', views.cat_stats, name='cat_stats'),
]
