from django.urls import path
import portfolio.views
from portfolio import views
from logofolio import views
from webfolio import views
from appfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio.views.home, name='home'),
    path('logo/', include('logofolio.urls')),
    path('web/', include('webfolio.urls')),
    path('app/', include('appfolio.urls')),

]
