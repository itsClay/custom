from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def endurance(request):
    return render(request, "endurance.html", {})

def energy(request):
    return render(request, "energy.html", {})

def strength(request):
    return render(request, "strength.html", {})
