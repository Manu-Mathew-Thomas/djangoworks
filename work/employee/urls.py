from django.urls import path
from . import views
app_name = "employee"  # 👈 real namespace lives here
urlpatterns = [
    path('', views.viewemployee, name='viewemployee'),
    path('add/', views.addemployee, name='addemployee'),
]