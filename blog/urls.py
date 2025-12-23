from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.blog_create, name='blog_create'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),
    path('<int:id>/edit/', views.blog_update, name='blog_update'),
    path('<int:id>/delete/', views.blog_delete, name='blog_delete'),
]
