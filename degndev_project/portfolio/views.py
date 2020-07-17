from django.shortcuts import render
from .models import portfolio
from django.contrib import messages

def home(request):
    portfolios = portfolio.objects
    return render(request,'portfolio/home.html', {'portfolios':portfolios})
