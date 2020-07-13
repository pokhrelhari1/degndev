from django.shortcuts import render
from .models import appfolio

def apps(request):
    appfolios = appfolio.objects
    return render(request,'appfolio/baseapp.html',{'appfolios':appfolios})
