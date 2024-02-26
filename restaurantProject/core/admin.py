from django.contrib import admin
from .models import Restuarants, Rating, Sales

# Register your models here.

admin.site.register(Restuarants)
admin.site.register(Rating)
admin.site.register(Sales)