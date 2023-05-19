from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name="home"),
    path('artists/', views.artists, name='artists'),
    path('artists_list/', views.artist_list, name='artists_list'),
    path('albums/', views.albums, name='albums'),
    path('albums_list/', views.album_after_year, name='albums_list'),
    path('genres/', views.genres, name='genres'),
    path('album2/', views.album_with_number, name='album2'),


]
