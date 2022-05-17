from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi my name is Amiriddin and this is a cars page")
