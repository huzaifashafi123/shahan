from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, "index.html")  # This loads your HTML file


def about(request):
    return render(request, "about.html") 

def resume(request):
    return render(request, "resume.html") 

def services(request):
    return render(request, "services.html") 

def portfolio(request):
    return render(request, "portfolio-details.html") 


def contact(request):
    return render(request, "contact.html") 

def packages(request):
    return render(request, "packages.html")