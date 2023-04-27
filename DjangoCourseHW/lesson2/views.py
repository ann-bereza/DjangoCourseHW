import requests
from django.http import HttpResponse
from django.shortcuts import render

API_KEY = '7c03630acc2d0be2f06224314bc8e825'


def index(request):
    return HttpResponse("<h1>This is a Index page<h1>")


def home(request):
    return HttpResponse("<h1>This is a Homepage<h1>")


def book(request, chapter):
    return HttpResponse(f"<h1>This is Chapter {chapter}<h1>")


def bio(request, username):
    return HttpResponse(f"<h1>This is a {username}'s bio <h1>")


def weather(request):
    city = request.GET.get('city')
    if not city:
        return HttpResponse('<script>alert("Please provide a city!"); window.location.href = "/";</script>')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponse(f'<script>alert("City {city} does not exist!"); window.location.href = "/";</script>')
    weather_data = response.json()
    print(weather_data)
    country = weather_data['sys']['country']
    city_name = weather_data['name']
    lon = weather_data['coord']['lon']
    lat = weather_data['coord']['lat']
    current_weather = weather_data['weather'][0]['description'].title()
    temp = weather_data['main']['temp']
    context = {
        'country': country,
        'city': city_name,
        'lon': lon,
        'lat': lat,
        'weather': current_weather,
        'temp': temp,
    }
    return render(request, 'lesson_2/weather.html', context)
