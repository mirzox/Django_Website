from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home2/', views.index_alt2, name='index_alt2'),
    path('home3/', views.index_alt3, name='index_alt3'),
    path('home4/', views.index_alt4, name='index_alt4'),
    path('homelanging/', views.index_landing, name='index_landing'),

    path('about/', views.about, name='about')
]
