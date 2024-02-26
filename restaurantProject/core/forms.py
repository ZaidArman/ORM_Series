from django import forms 
from core.models import Restuarants
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