from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def main_view(request):
    return render(request, 'main.html')


def departure_view(request):
    return render(request, 'departure.html')


def tour_view(request):
    return render(request, 'tour.html')
