from django.shortcuts import render
from .models import webfolio

def webs(request):
    webfolios = webfolio.objects
    return render(request,'webfolio/baseweb.html',{'webfolios':webfolios})


# Create your views here.
