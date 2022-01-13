from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home2/', views.index_alt2, name='index_alt2'),
    path('home3/', views.index_alt3, name='index_alt3'),
    path('home4/', views.index_alt4, name='index_alt4'),
    path('homelanging/', views.index_landing, name='index_landing'),
    path('typography/', views.typography, name='typography'),
    path('components/', views.components, name='components'),
    path('icons/', views.icons, name='icons'),
    path('icons2/', views.icons2, name='icons2'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('team/', views.team, name='team'),
    path('services/', views.services, name='services'),
    path('pricingbox/', views.pricingbox, name='pricingbox'),
    path('404/', views.page404, name='404'),
]
