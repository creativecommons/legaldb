from django.shortcuts import render # noqa
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the CC Legal Database project index.")
