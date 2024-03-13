from django.contrib import admin
from .models import Restuarants, Rating, Sales, Product, Order, Comment


# for GenericForeingKey
class RestuarantAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name'
    ]
    
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