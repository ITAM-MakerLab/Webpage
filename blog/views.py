from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, "blog/homepage.html")


def hola(request):
    return HttpResponse("Hola amigo. Has llegado lejos")
