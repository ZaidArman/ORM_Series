from typing import Any
from django import forms 
from core.models import Restuarants, Order
from django.core.validators import MinValueValidator, MaxValueValidator

# class ratingForm(forms.Form):
    # class Meta:
    #     model = Rating
    #     fields = ('restuarant', 'user', 'rating')
    # rating = forms.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    
class restuarantForm(forms.ModelForm):
    class Meta:
        model = Restuarants
        fields = ('name', 'restuarant_type',)
        

""" create an exception if there are no product in stock """
class ProductStockException(Exception):
    pass

""" form for product that we will order """
class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
    # function to save and check either product ia aviable or not
    def save(self, commit=True):
        order = super().save(commit=False) # check to see if the product has anough items in stock
        if order.product_order.number_in_stock < order.number_of_items:
            raise ProductStockException(
                f"Not anough items in stock for that product: {order.product_order}"
            )
        if commit:
            order.save()
        return order
    