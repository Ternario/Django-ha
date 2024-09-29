from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    your_name = "Andrii"
    return HttpResponse(f"Hello, {your_name}")
