from django.urls import path
from lesson2 import views

urlpatterns = [
    path('index/', views.index, name="index-view"),
    path('home/', views.home, name="home-view"),
    path('book/<str:chapter>', views.book, name="book"),
    path('bio/<str:username>', views.bio, name="bio"),
    path('weather/', views.weather, name='weather'),
]