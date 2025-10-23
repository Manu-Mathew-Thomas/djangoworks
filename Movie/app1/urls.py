from django.urls import path
from . import views

app_name = "app1"  # 👈 real namespace lives here
urlpatterns = [
    path('', views.movielist, name='movielist'),
    path('add/', views.addmovie, name='addmovie'),
]