from django.shortcuts import render

from .models import portfolio

def home(request):
    portfolios = portfolio.objects
    return render(request,'portfolio/home.html', {'portfolios':portfolios})

# def team(request):
#     return render('portfolio/team.html', {'teams':teams})

# def team(request):
#     return render(request,'portfolio/team.html')
