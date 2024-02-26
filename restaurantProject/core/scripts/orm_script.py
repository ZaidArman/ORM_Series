from django.contrib.auth.models import User
from core.models import Restuarants, Rating, Sales
from django.utils import timezone
from django.db import connection

def run():
# use to print the first element in the database
    # print(Restuarants.objects.last())
    
# use to print the first element in the database
    # print(Restuarants.objects.first())
    
# use to count the number of rows in database
    # print(Restuarants.objects.count())
    
#we can easily create & save each time when we run the script
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
    
# now we are going to work with User and Rating Models
    # restuarant = Restuarants.objects.last()
    # user = User.objects.first()
    # # give rating to the Restuarant n0 last from user 1
    # Rating.objects.create(user=user, restuarant=restuarant, rating=5) 
    # print(Rating.objects.all())
    
# Using filter()
    # print(Rating.objects.filter(rating=5))
    # print(Rating.objects.filter(rating__gte=3)) # __gte mean: greater than or equal to 3
    # print(Rating.objects.filter(rating__lte=3)) # __lte mean: less than or equal to 3
    
#exclude function: Returns a new QuerySet containing objects that do not match the given lookup parameters
    # print(Rating.objects.exclude(rating__gte=3)) # exclude() mean:  WHERE NOT ratong greater/equal 3
    # print(connection.queries)
    
# if we want to print the rating of all associated restuuarants, we can use rating_set manager
    # restuarant = Restuarants.objects.first()
    # print(restuarant.rating_set.all())
    
# now adding sale value to a sale table
    # Sales.objects.create(
    #     restuarant = Restuarants.objects.first(),
    #     income = 5.89,
    #     datetime = timezone.now()        
    # )
    
# retrieve the sales data of restuarant(1) with related_name=sales
    # restuarant = Restuarants.objects.first()
    # print(restuarant.sales.all())
    
# uses of get_or_create() method
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
    
#use to check min-max value validators for rating
    # user = User.objects.first()
    # restuarant = Restuarants.objects.first()
    # rating = Rating(user=user, restuarant=restuarant, rating=9)
    # rating.full_clean()
    # rating.save()
    
# updating the existing records
    # restuarant = Restuarants.objects.first()
    # print(restuarant.name)
    # restuarant.name = 'New restuarant name'
    # restuarant.save(update_fields=['name'])
    # print(restuarant.name)
    
# now we going to create a new restuarant to check the True value of save method
    # restuarant = Restuarants()
    # restuarant.name = 'The Turkish Restuarant # 3'
    # restuarant.latitude = 10.2
    # restuarant.longitude = -67.90
    # restuarant.date_opened = timezone.now()
    # restuarant.restuarant_type = Restuarants.TypeChoices.TURKEY
    # restuarant.save()
    
# update single attributes like date_opened:
    # restuarant = Restuarants.objects.all()
    # restuarant.update(
    #     date_opened = timezone.now()
    # )
    
# to update multiple attributes date_opened and website   
    # restuarant = Restuarants.objects.filter(name__startswith='T')
    # print(restuarant)
    # restuarant.update(
    #     date_opened = timezone.now() - timezone.timedelta(days=365),
    #     website = 'www.restuarants.com'
    # )
    
# Delete method
    # restuarant = Restuarants.objects.first()
    # # print the Primary-Key of resturant
    # print(restuarant.pk)
    # # print the Primary-Key of resturant from rating
    # print(restuarant.ratings.all())
    # # delete the restuarant from restuarant table and also from rating tables
    # restuarant.delete()
    
# delete all objects
    # Restuarants.objects.all().delete()
    # print(connection.queries)
    
# count data that we enter from commands
    # print(Restuarants.objects.count())
    # print(Rating.objects.count())
    # print(Sales.objects.count())
    
# filter only Chinese restuarants
    # print(Restuarants.objects.filter(restuarant_type=Restuarants.TypeChoices.CHINESE))
    # print(Restuarants.objects.filter(name='Pizzeria 1'))
    # print(connection.queries)
    
# in lookup 
    # pakistan = Restuarants.TypeChoices.PAKISTAN
    # india = Restuarants.TypeChoices.INDIAN
    # china = Restuarants.TypeChoices.CHINESE
    
    # in_lookup_check = [pakistan, india, china]
    # restuarant = Restuarants.objects.filter(restuarant_type__in=in_lookup_check)
    # print(restuarant)
    # print(connection.queries)

# exclude method with in-lookup
    # india = Restuarants.TypeChoices.INDIAN
    # china = Restuarants.TypeChoices.CHINESE
    # restuarant = Restuarants.objects.exclude(restuarant_type__in=[china, india])
    # print(restuarant)
    # print(connection.queries)
    
# less than lookup ( __lt )
    # restuarant = Restuarants.objects.filter(name__lt='K')
    # print(restuarant)

# greater than lookup ( __gt )
    # restuarant = Restuarants.objects.filter(latitude__gt=2.00)
    # print(restuarant)

# range lookup (range)
    # restuarant = Restuarants.objects.filter(latitude__range=(20, 80))
    # print(restuarant)

# ordered_by() with descending
    # restuarant = Restuarants.objects.order_by('name').reverse()
    # print(restuarant)

# earliest ( return a single first value) & latest functions
    # restuarant = Restuarants.objects.earliest('date_opened')
    # restuarant1 = Restuarants.objects.latest('date_opened')
    # print(restuarant)
    # print(restuarant1)
    
# inner join a object with specific object
    # chinese = Restuarants.TypeChoices.CHINESE
    # sale = Sales.objects.filter(restuarant__restuarant_type=chinese)
    # print(sale)
    # print(connection.queries)
    pass