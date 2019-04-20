from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage.as_view(), name='homepage'),
    path('contacts/', views.contacts, name='contacts'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail')
]
