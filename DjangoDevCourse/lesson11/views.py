from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>This is a Homepage</h1>")


def les_1_1(request):
    return render(request, "lesson11/index.html")
