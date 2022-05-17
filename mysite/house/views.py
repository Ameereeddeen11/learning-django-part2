from django.shortcuts import render
from django.http import HttpResponse

def indexhome(request):
    return HttpResponse("Hi my name is Amiriddin and this is house page")
