from django.contrib import admin
from .models import Restuarants, Rating, Sales, Product, Order, Comment
from django.contrib.contenttypes.admin import GenericTabularInline

""" Using generic relations as an inline
If you want to allow editing and creating an Comment instance on the Restuarant, add/change 
views you can use GenericTabularInline or GenericStackedInline (both subclasses of 
GenericInlineModelAdmin) provided by admin. 
They implement tabular and stacked visual layouts for the forms representing the inline objects, 
respectively, just like their non-generic counterparts. They behave just like any other inline. 
In your admin.py for this example app:
"""
class CommentInline(GenericTabularInline):
    model = Comment
    max_num = 1 # It's a box time range, we can change

# for GenericForeingKey
class RestuarantAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name'
    ]
    inlines = [CommentInline] # to attach the comment with restuarant
    
class RatingAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'rating'
    ]
    
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'comment_text', 'object_id', 'content_type', 'content_object'
    ]

admin.site.register(Restuarants, RestuarantAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Sales)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment, CommentAdmin) # for GenericForeingKey