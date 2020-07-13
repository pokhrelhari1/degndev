from django.shortcuts import render
from .models import logofolio

def logos(request):
    logofolios = logofolio.objects
    return render(request,'logofolio/baselogo.html',{'logofolios':logofolios})
