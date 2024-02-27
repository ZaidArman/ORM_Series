from django.contrib.auth.models import User
from core.models import Restuarants, Rating, Sales, Staff, StaffRestuarant
from django.utils import timezone
from django.db import connection
from django.db.models import F, Count, Avg, Min, Max, Sum
from django.db.models.functions import Upper
import random

def run():
    """ use to print the first element in the database """
    # print(Restuarants.objects.last())
    
    """ use to print the first element in the database """
    # print(Restuarants.objects.first())
    
    """ use to count the number of rows in database """
    # print(Restuarants.objects.count())
    
    """ we can easily create & save each time when we run the script """
    # Restuarants.objects.create(
    #     name = 'The Food Restuarant',
    #     latitude = 1.2,
    #     longitude = 16.90,
    #     date_opened = timezone.now(),
    #     restuarant_type = Restuarants.TypeChoices.INDIAN,
    # )
    # print(connection.queries)
    
    # restuarant = Restuarants.objects.all()[0:3]
    # print(restuarant)
    # print(connection.queries)
    
    # restuarant = Restuarants()
    # restuarant.name = 'The Turkish Restuarant'
    # restuarant.latitude = 10.2
    # restuarant.longitude = -67.90
    # restuarant.date_opened = timezone.now()
    # restuarant.restuarant_type = Restuarants.TypeChoices.TURKEY
    # restuarant.save()
    
    """ now we are going to work with User and Rating Models """
    # restuarant = Restuarants.objects.last()
    # user = User.objects.first()
    # # give rating to the Restuarant n0 last from user 1
    # Rating.objects.create(user=user, restuarant=restuarant, rating=5) 
    # print(Rating.objects.all())
    
    """ Using filter() """
    # print(Rating.objects.filter(rating=5))
    # print(Rating.objects.filter(rating__gte=3)) # __gte mean: greater than or equal to 3
    # print(Rating.objects.filter(rating__lte=3)) # __lte mean: less than or equal to 3
    
    """ exclude function: Returns a new QuerySet containing objects that do not match the given lookup parameters """
    # print(Rating.objects.exclude(rating__gte=3)) # exclude() mean:  WHERE NOT ratong greater/equal 3
    # print(connection.queries)
    
    """ if we want to print the rating of all associated restuuarants, we can use rating_set manager """
    # restuarant = Restuarants.objects.first()
    # print(restuarant.rating_set.all())
    
    """ now adding sale value to a sale table """
    # Sales.objects.create(
    #     restuarant = Restuarants.objects.first(),
    #     income = 5.89,
    #     datetime = timezone.now()        
    # )
    
    """ retrieve the sales data of restuarant(1) with related_name=sales """
    # restuarant = Restuarants.objects.first()
    # print(restuarant.sales.all())
    
    """ uses of get_or_create() method """
    # user = User.objects.first()
    # restuarant = Restuarants.objects.first()
    # rating , created = Rating.objects.get_or_create(
    #     restuarant=restuarant,
    #     user = user,
    #     rating = 4.5
    # )
    # if created:
    #     # send email if user created
    #     pass
    
    """ use to check min-max value validators for rating """
    # user = User.objects.first()
    # restuarant = Restuarants.objects.first()
    # rating = Rating(user=user, restuarant=restuarant, rating=9)
    # rating.full_clean()
    # rating.save()
    
    """ updating the existing records """
    # restuarant = Restuarants.objects.first()
    # print(restuarant.name)
    # restuarant.name = 'New restuarant name'
    # restuarant.save(update_fields=['name'])
    # print(restuarant.name)
    
    """ now we going to create a new restuarant to check the True value of save method """
    # restuarant = Restuarants()
    # restuarant.name = 'The Turkish Restuarant # 3'
    # restuarant.latitude = 10.2
    # restuarant.longitude = -67.90
    # restuarant.date_opened = timezone.now()
    # restuarant.restuarant_type = Restuarants.TypeChoices.TURKEY
    # restuarant.save()
    
    """ update single attributes like date_opened: """
    # restuarant = Restuarants.objects.all()
    # restuarant.update(
    #     date_opened = timezone.now()
    # )
    
    """ to update multiple attributes date_opened and website """
    # restuarant = Restuarants.objects.filter(name__startswith='T')
    # print(restuarant)
    # restuarant.update(
    #     date_opened = timezone.now() - timezone.timedelta(days=365),
    #     website = 'www.restuarants.com'
    # )
    
    """ Delete method """
    # restuarant = Restuarants.objects.first()
    # # print the Primary-Key of resturant
    # print(restuarant.pk)
    # # print the Primary-Key of resturant from rating
    # print(restuarant.ratings.all())
    """ delete the restuarant from restuarant table and also from rating tables """
    # restuarant.delete()
    
    """ delete all objects """
    # Restuarants.objects.all().delete()
    # print(connection.queries)
    
    """ count data that we enter from commands """
    # print(Restuarants.objects.count())
    # print(Rating.objects.count())
    # print(Sales.objects.count())
    
    """ filter only Chinese restuarants """
    # print(Restuarants.objects.filter(restuarant_type=Restuarants.TypeChoices.CHINESE))
    # print(Restuarants.objects.filter(name='Pizzeria 1'))
    # print(connection.queries)
    
    """ in lookup """
    # pakistan = Restuarants.TypeChoices.PAKISTAN
    # india = Restuarants.TypeChoices.INDIAN
    # china = Restuarants.TypeChoices.CHINESE
    
    # in_lookup_check = [pakistan, india, china]
    # restuarant = Restuarants.objects.filter(restuarant_type__in=in_lookup_check)
    # print(restuarant)
    # print(connection.queries)

    """ exclude method with in-lookup """
    # india = Restuarants.TypeChoices.INDIAN
    # china = Restuarants.TypeChoices.CHINESE
    # restuarant = Restuarants.objects.exclude(restuarant_type__in=[china, india])
    # print(restuarant)
    # print(connection.queries)
    
    """ less than lookup ( __lt ) """
    # restuarant = Restuarants.objects.filter(name__lt='K')
    # print(restuarant)

    """ greater than lookup ( __gt ) """
    # restuarant = Restuarants.objects.filter(latitude__gt=2.00)
    # print(restuarant)

    """ range lookup (range) """
    # restuarant = Restuarants.objects.filter(latitude__range=(20, 80))
    # print(restuarant)

    """ ordered_by() with descending """
    # restuarant = Restuarants.objects.order_by('name').reverse()
    # print(restuarant)
    
    """ ordered by random/custom ordered """
    # restaurants = Restuarants.objects.annotate(random_order=F('id') % 100).order_by('random_order')
    # restaurants = Restuarants.objects.annotate(random_order=F('id') % 100).order_by('?')
    # print(restaurants)

    """ earliest ( return a single first value) & latest functions """
    # restuarant = Restuarants.objects.earliest('date_opened')
    # restuarant1 = Restuarants.objects.latest('date_opened')
    # print(restuarant)
    # print(restuarant1)
    
    """ inner join a object with specific object """
    # chinese = Restuarants.TypeChoices.CHINESE
    # sale = Sales.objects.filter(restuarant__restuarant_type=chinese)
    # print(sale)
    
    """ Handling Many2Many Relationship from staff side"""
    # staff, created = Staff.objects.get_or_create(staff_name='Zaid')
    # print(staff)
    """ Here we want to retrieve all the staff member that are working with restuarants
        but it show zero, bcz we created but not associate with them """
    # print(staff.restuarant.all())
    
    """ add() # associate or add the element to the related model """
    # staff.restuarant.add(Restuarants.objects.first()) # Associate staff with restuarant
    # print(staff.restuarant.all()) # now we associate it and it will show staff with restuarant

    """ set(): will set the range of associate & count: will count """
    # staff.restuarant.set(Restuarants.objects.all()[:5])
    # print(staff.restuarant.count()) # will count
    
    """ remove() # will remove only one associate """
    # staff.restuarant.remove(Restuarants.objects.first())
    # print(staff.restuarant.count()) # will count
    
    """ clear(): """
    # staff.restuarant.clear() # will clear all the associate object
    # print(staff.restuarant.count()) # will count
    
    """ from restuarant Side:
        here we are going to create 1 staff with associate 2 different resturants
    """
    # staff, created = Staff.objects.get_or_create(staff_name='Kaabir Singh')
    # restuarant = Restuarants.objects.first() # associate with first resturant (date_opened) ordered
    # restuarant2 = Restuarants.objects.last() # associate with last restuarant (date-opened) ordered
    
    # StaffRestuarant.objects.create(
    #     staff=staff, restuarant=restuarant, salary=28_000
    # )
    
    # StaffRestuarant.objects.create(
    #     staff=staff, restuarant=restuarant2, salary=40_000
    # )

    """ now try to checkout from staff side using through method """
    # staff, created = Staff.objects.get_or_create(staff_name='Kaabir Singh')
    # staff.restuarant.clear() # clear old values
    
    # restuarant = Restuarants.objects.first()
    # staff.restuarant.add(restuarant, through_defaults={'salary':90_000}) # associate and add salary
    
    """ if we want to associate with first 10 restuarants, """
    # staff, created = Staff.objects.get_or_create(staff_name='Kaabir Singh')
    # staff.restuarant.set(
    #     Restuarants.objects.all()[0:10], 
    #     through_defaults={'salary':random.randint(20_000, 10_000_0)}
    #     )

    """values():
        Returns a QuerySet that returns dictionaries, rather than model instances, when used as an iterable.
        Each of those dictionaries represents an object, with the keys corresponding to the attribute names of model objects
    """
    """  will only return the dict of first row with name and date_opened """
    # restuarant = Restuarants.objects.values('name', 'date_opened').first() 
    
    """ will return the queryset of all row with name and date_opened """
    # restuarant = Restuarants.objects.values('name', 'date_opened')

    """ Transforming values with DB functions """
    # restuarant = Restuarants.objects.values(name_upper=Upper('name'))[:3]
    # print(restuarant)
    
    """ Getting ForeingKey data with values() """
    # IT = Restuarants.TypeChoices.ITALIAN
    # rating = Rating.objects.filter(restuarant__restuarant_type=IT).values('rating', 'restuarant__name')
    # print(rating)
    
    """ values_list():
        This is similar to values() except that instead of returning dictionaries, 
        it returns tuples when iterated over. 
        Each tuple contains the value from the respective field or 
        expression passed into the values_list() call — so the first item is the first field, etc
    """
    # restuarant = Restuarants.objects.values_list('name', 'date_opened)
    # restuarant = Restuarants.objects.values_list('name', flat=True) # flat use for returning list
    # print(restuarant)
    
    """ aggregate function:
        aggregate() is a terminal clause for a QuerySet that, when invoked, returns a dictionary of name-value pairs. 
        The name is an identifier for the aggregate value; the value is the computed aggregate. 
        The name is automatically generated from the name of the field and the aggregate function. 
        If you want to manually specify a name for the aggregate value, 
        you can do so by providing that name when you specify the aggregate clause.
    """
    """ suppose we want to achieve this """
    # restuarant = Restuarants.objects.filter(name__istartswith='c').count() 
    # print(restuarant)
    """ we can also do using aggregate """
    # restuarant = Restuarants.objects.aggregate(total_id=Count('id')) # total_id is just a name/ we can do without this name
    # print(restuarant)

    """ aggregate with Min & Max, Avg, Sum """
    # income_min_max = Sales.objects.aggregate(
    #     minimum=Min('income'), 
    #     maximum=Max('income'),
    #     Average=Avg('income'),
    #     total=Sum('income')
    #     )
    # print(income_min_max)
    
    """ if we want to print the last month income of aggregating, then """
    one_month_sale = timezone.now() - timezone.timedelta(days=31)
    sale = Sales.objects.filter(datetime__gte=one_month_sale)
    income_min_max = sale.aggregate(
        minimum=Min('income'),
        maximum=Max('income'),
        Average=Avg('income'),
        total=Sum('income')
        )
    print(income_min_max)