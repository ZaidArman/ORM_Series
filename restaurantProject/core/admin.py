from django.contrib import admin
from .models import Restuarants, Rating, Sales, Product, Order

# Register your models here.

admin.site.register(Restuarants)
admin.site.register(Rating)
admin.site.register(Sales)
admin.site.register(Product)
admin.site.register(Order)