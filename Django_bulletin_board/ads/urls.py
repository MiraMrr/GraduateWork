from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_ad, name='create'),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete'),
]
