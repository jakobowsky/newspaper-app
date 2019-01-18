# articles/urls.py
from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
) 

urlpatterns = [
    path('<ink:pk>/edit/',
    ArticleUpdateView.as_view(), name='article_edit'),
    path('<ink:pk>/',
    ArticleDetailView.as_view(), name='article_detail'),
    path('<ink:pk>/delete/',
    ArticleDeleteView.as_view(), name='article_delete'),
    path('', ArticleListView.as_view(), name='article_list')
]
