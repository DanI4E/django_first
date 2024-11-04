from django.urls import path
from public_app import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    path('photo/', views.photo, name='photo')
]