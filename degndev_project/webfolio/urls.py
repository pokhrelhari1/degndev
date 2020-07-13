from django.urls import path
from . import views

urlpatterns = [
    path('',views.webs, name='webs'),
]
