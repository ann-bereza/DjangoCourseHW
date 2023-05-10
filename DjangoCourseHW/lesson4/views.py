from django.http import HttpResponse


# Create your views here.
def main(request):
    return HttpResponse(f"<h1>This is a main page.</h1>")
