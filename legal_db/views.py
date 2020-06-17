from django.shortcuts import render  # noqa
from django.http import HttpResponse


def index(request):
    return render(request, "legal_db/index.html")

