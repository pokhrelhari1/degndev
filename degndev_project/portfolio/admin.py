from django.contrib import admin
from .models import portfolio


# admin.site.site_header = 'DEGnDEV'
admin.site.site_title = 'Database'
admin.site.register(portfolio)
