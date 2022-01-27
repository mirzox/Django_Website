from django.urls import path

from .views import CategoryView, CategoryDetailView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view())
]
