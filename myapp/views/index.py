# myapp/views/index.py
from django.shortcuts import render


def index(request):
    return render(request, "index.html")
