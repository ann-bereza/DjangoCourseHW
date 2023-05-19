from django.http import HttpResponse
from django.shortcuts import render

from .models import Artist, Album, Genre


def main(request):
    return HttpResponse(f"<h1>This is a main page.</h1>")


def artists(request):
    artists = Artist.objects.all()
    return render(request, 'lesson6/artist.html', {'artists': artists})


def albums(request):
    albums = Album.objects.all()
    return render(request, 'lesson6/album.html', {'albums': albums})


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'lesson6/genre.html', {'genres': genres})


def artist_list(request):
    query = request.GET.get('query', '')
    if query:
        artists = Artist.objects.filter(name__istartswith=query)
        return render(request, 'lesson6/artist_list.html', {'artists': artists})
    else:
        return HttpResponse(f"<h3>Nothing was found.</h3>")


def album_after_year(request):
    query = request.GET.get('query', '')
    if query:
        albums = Album.objects.filter(release_date__year__gt=query)
        return render(request, 'lesson6/album.html', {'albums': albums})
    else:
        return HttpResponse(f"<h3>Nothing was found.</h3>")


def album_with_number(request):
    albums = Album.objects.filter(title__contains='2')
    return render(request, 'lesson6/album.html', {'albums': albums})


