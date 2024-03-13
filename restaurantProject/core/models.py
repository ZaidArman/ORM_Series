from typing import Any
from django.db import models
from django.contrib.auth.models import User # will use the Build-In Model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower

""" We are gointg to create 4 models: 
    # Restuarants
    # User :- will use the BuildIn Model
    # rating
    # Sales
    # Staff :- M2M relationship Model/Table with Restuarants
    # StaffRestuarant :- A Conjuction Model/Table
"""

""" custo Validators for restuarant name """
def restuarant_name_begin_with_a(value):
    if not value.startswith('a'):
        raise ValidationError('Restuarant name must be begin with "a" ')

""" Restuarant Model to store data about restuarant"""
class Restuarants(models.Model):
    class TypeChoices(models.TextChoices):
        PAKISTAN = "PAK", "Pakistan"
        INDIAN = "IND", "Indian"
        CHINESE = "CHI", "Chinese"
        ITALIAN = "ITA", "Italian"
        TURKEY = "TRK", "Turkey"
        ARABIAN = "ARB", "ARAB"
        SPANISH = "SPN", "Spanish"
        OTHER = "OTR", "Other Food"    
    
    name = models.CharField(max_length=100, validators=[restuarant_name_begin_with_a]) # name startswith a
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField(
        validators = [MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        validators = [MinValueValidator(-180), MaxValueValidator(180)]
    )
    restuarant_type = models.CharField(max_length=3, choices=TypeChoices.choices)
    # for handling Null Values in DB
    capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True)
    
    # class Meta:
    #     """ here wo do by defualt ordering with lower case name """
    #     ordering = [Lower('date_opened')]
    #     get_latest_by = 'date_opened' # by defualt show the last value ordered by date_opened
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)

""" A staff model that have M2M relationship"""
class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    restuarant = models.ManyToManyField(Restuarants, through='StaffRestuarant')
    
    def __str__(self):
        return self.staff_name
    
"""
A model/table (Conjuction), where, if we want to create a custom seperate table between Staff & Restuarant for (M2M relaationship), 
for that we can use Through method
"""
class StaffRestuarant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restuarant = models.ForeignKey(Restuarants, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)

""" Rating Model to store data about Rating of Costumers """
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restuarant = models.ForeignKey(Restuarants, on_delete=models.CASCADE, related_name='ratings')
    
    """ Use Min and max Field-Validator """
    rating = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"Rating {self.rating}"


""" Sales Model to store data about Sales """
class Sales(models.Model):
    restuarant = models.ForeignKey(Restuarants, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expendature = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
    

""" Database Transactions:
    Now we going to working on Database Transactions, for that we are going to create the bellow models 
"""

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    number_in_stock = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    product_order = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_items = models.PositiveSmallIntegerField()
    # user
    
    def __str__(self) -> str:
        return f"{self.number_of_items} x {self.product_order.product_name}"
    
# for GenericForeingKey
class Comment(models.Model):
    comment_text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")