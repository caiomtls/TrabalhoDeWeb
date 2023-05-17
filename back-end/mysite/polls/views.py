from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'teste.html', {"nome":"aaaa", "trails":["a","b","c"]})