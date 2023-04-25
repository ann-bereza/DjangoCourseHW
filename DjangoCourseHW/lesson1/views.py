from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "lesson1/hello.html")


def les_1_1(request):
    return render(request, "lesson1/index.html")
