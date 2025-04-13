from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← это главная страница по "/"
    path('list/', views.films_list, name='films_list'),
    path('add/', views.add_film, name='add_film'),
]
