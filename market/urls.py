from django.urls import path

from .views import (CategoryView, CategoryDetailView, BrandView, BrandDetailView, NotebookView, NotebookDetailView,
                    NotebookApiView, NotebookDetailApiView)

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('brand/', BrandView.as_view()),
    path('brand/<int:pk>/', BrandDetailView.as_view()),
    path('notebook/', NotebookView.as_view()),
    path('notebook/<int:pk>/', NotebookDetailView.as_view()),

    path('notebookdetail/', NotebookApiView.as_view()),
    path('notebookdetail/<int:pk>/', NotebookDetailApiView.as_view())
]
