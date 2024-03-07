from django.contrib.auth.models import User
from core.models import Restuarants, Rating, Sales, Staff, StaffRestuarant
from django.utils import timezone
from django.db import connection
from django.db.models import F, Count, Avg, Min, Max, Sum, Value, CharField, F, Q
from django.db.models.functions import Upper, Length, Concat
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
    # one_month_sale = timezone.now() - timezone.timedelta(days=31)
    # sale = Sales.objects.filter(datetime__gte=one_month_sale)
    # income_min_max = sale.aggregate(
    #     minimum=Min('income'),
    #     maximum=Max('income'),
    #     Average=Avg('income'),
    #     total=Sum('income')
    #     )
    # print(income_min_max)
    
    
    """ 28 / 02 / 2024
    Annotate():
    Per-object summaries can be generated using the annotate() clause. When an annotate() clause is specified, 
    each object in the QuerySet will be annotated with the specified values.
    """
    # ToDo:
    """
    Fetch all restuarants, and let's assume, if we want to retrieve the number of characters in the name of restuarant
    """
    # restuarant = Restuarants.objects.annotate(name_len=Length('name')).filter(name_len__gte=10) # print name that length greater than 10
    # print(restuarant.values('name', 'name_len')) # number of character of the restuarant using annotate
    
    """
    if we want to print the name of restuarants with ratings: like thi
    "Restuarant1 [Rating: 3.5]" so let's do it!
    """
    # concatenation = Concat(
    #     'name',
    #     Value(' [Rating: '),
    #     Avg('ratings__rating'),
    #     Value(']'), # already import:- from django.db.models import Value
    #     output_field = CharField() # already import:- from django.db.models import CharField
    #     )
    # restuarant = Restuarants.objects.annotate(message=concatenation)
    # for r in restuarant:
    #     print(r.message)
    
    """
    if we want to print the sales(incomee) of the restuarants using annotate
    """
    # restuarant = Restuarants.objects.annotate(total_sale=Sum('sales__income'))
    # restaurant = [{'name': r.name, 'total_sale': r.total_sale} for r in restuarant]
    # print(restaurant)
    
    # restuarant = Restuarants.objects.annotate(total_sale=Sum('sales__income')).order_by('total_sale').filter(total_sale__lt=400)
    # for r in restuarant:
    #     print(r.total_sale)
    
    """ To use aggregate on the annotate values """
    # restuarant = Restuarants.objects.annotate(total_sale=Sum('sales__income')).order_by('total_sale').filter(total_sale__lt=400)
    # print(restuarant.aggregate(average_sale=Avg('total_sale')))
    
    """
    now if we want to fetch the number for ratings and averae_ratings for restuarants using annotate
    """
    # restuarant = Restuarants.objects.annotate(
    #     num_ratings=Count('ratings'),
    #     average_rating=Avg('ratings__rating')
    #     )
    # print(restuarant.values('name', 'num_ratings', 'average_rating'))
    """ Print the ratings based on Restuarant types (grouping) """
    # restuarant = Restuarants.objects.values('restuarant_type').annotate(
    #     num_ratings=Count('ratings')
    #     )
    # print(restuarant)
    

    """ F() Object:
    An F() object represents the value of a model field, transformed value of a model field, or annotated column. 
    It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.
    Instead, Django uses the F() object to generate an SQL expression that describes the required operation at the database level.
    """
    # let's see the example
    # rating = Rating.objects.filter(rating=3).all()
    # print(rating) # Output: 3
    """ if we want to update the rating +1, then """
    """ one-way in python using Increment way """
    # rating.rating += 1
    """ instead of increment we can use F() """
    # rating = F('rating') + 1 # it will add value of 1
    # print(rating) # Output: 4
    
    """ If we want to update the ratings from 5 start to 10, we can do using F() """
    # Rating.objects.update(rating=F('rating') / 2) # using / we can back to original ratings
    # print(connection.queries)
    
    # sale = Sales.objects.all()
    # for s in sale:
    #     s.expendature = random.uniform(5, 100)
    """ Update in bulk¶
    When updating objects, where possible, use the bulk_update() method to reduce the number of SQL queries. Given a list or queryset of objects: 
    """
    # Sales.objects.bulk_update(sale, ['expendature'])
    
    """ using F() with filter method """
    # sale = Sales.objects.filter(expendature__gt=F('income'))
    # print(sale)
    # print(connection.queries)
    
    """ using F() with annotate method 
    If we want to check the profit from income of sales for the restuarants
    """
    # sale = Sales.objects.annotate(profit = F('income') - F('expendature')).order_by('profit')
    # print(sale.last().profit) # print the last restuarant profit from sales
    
    """
    If we want to print the profit and loss of a restuarant using aggregate with Count, Q, F objects
    """
    # sale = Sales.objects.aggregate(
    #     profit = Count('id', filter=Q(income__gt=F('expendature'))),
    #     loss = Count('id', filter=Q(income__lt=F('expendature')))
    #     )
    # print(sale)
    
    """ refresh_from_db() : CombinedExpresion """
    # rating = Rating.objects.first()
    # print(type(rating))
    # print(type(Rating.objects.all()))
    # print(rating.rating)
    # rating.rating = F('rating') + 1
    # rating.save()
    # print(type(rating.rating)) # this output will show the CombinedExpression
    # rating.refresh_from_db() # this function refresh the db and update the value
    # print(rating.rating)
    
    
    # rating = rating.objects.all()
    # print(rating.rating)
    # rating.rating = F('rating') + 1
    # rating.save()
    # print(rating.rating) 
    
    """ Q() Object
    Keyword argument queries – in filter(), etc. – are “AND”ed together. 
    If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.
    A Q() object (django.db.models.Q) is an object used to encapsulate a collection of keyword arguments. 
    These keyword arguments are specified as in “Field lookups” above.
    
    Q objects can be combined using the &, |, and ^ operators. When an operator is used on two Q objects, it yields a new Q object.
    For example, this statement yields a single Q object that represents the “OR” of two "question__startswith" queries:
    """
    
    """ here if we want to print IND OR CHI restuarant """
    # IND = Restuarants.TypeChoices.INDIAN
    # CHI = Restuarants.TypeChoices.CHINESE
    # restuarant = Restuarants.objects.filter(
    #     Q(restuarant_type=IND) | # | is OR Operator
    #     Q(restuarant_type=CHI)
    # )
    # print(restuarant)
    
    """ a single queryset show "like" in SQL """
    # restuarant = Restuarants.objects.filter(
    #     name__icontains='1'
    # )
    # restuarant2 = Restuarants.objects.filter(
    #     name__iendswith='1'
    # )
    # print(restuarant, restuarant2)
    
    """ if we want to check the name contain indian or name contain chinese """
    # restuarant = Restuarants.objects.filter(
    #     Q(name__icontains="Indian") | Q(name__icontains="Chinese")
    # )
    # for r in restuarant:
    #     print(r.name)
    
    """ we can also use complex query like this with Q object """
    # IND_OR_CHI = Q(name__icontains="Indian") | Q(name__icontains="Chinese")
    # recent_opened = Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40))
    # not_recent_opened = ~Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40)) # using Not
    
    # restuarant = Restuarants.objects.filter( IND_OR_CHI | not_recent_opened )
    # print(restuarant)
    
    """ We want to find all sales, Where;
        - profit is greater than expendature OR
        - restuarant name contain a number
    """
    # name_has_num = Q(restuarant__name__regex=r"[0-9]+")
    # profited = Q(income__gt=F('expendature'))
    # sales = Sales.objects.filter(name_has_num | profited)
    # for s in sales:
    #     if s.income <= s.expendature:
    #         print(s.restuarant.name)
    
    """ We can also more examples like this """
    # name_has_num = Q(restuarant__name__regex=r"[0-9]+")
    # profited = Q(income__gt=F('expendature'))
    # sales = Sales.objects.filter(name_has_num | profited) # OR Operator
    # sales2 = Sales.objects.select_related('restuarant').filter(name_has_num & profited) # AND Operator
    
    # print(sales.count(), sales2.count())
    
    """
    Handling null values
    """
    # restuarant1 = Restuarants.objects.first()
    # restuarant2 = Restuarants.objects.last()
    # restuarant1.capacity = 10 # adding capacity to the first row
    # restuarant2.capacity = 20 # adding capacity to the last row
    # restuarant1.save()
    # restuarant2.save()
    # null_handling = Restuarants.objects.filter(capacity__isnull=False).count()
    # print(null_handling)
    
    """ Ordering by Capacity with Null Values """
    # null_handling = Restuarants.objects.order_by('capacity').values('capacity')
    # print(null_handling)
    """ Sort null values using F() """
    # null_handling = Restuarants.objects.order_by(F('capacity').asc(nulls_last=True)).values('capacity')
    # print(null_handling) 
    """ Output:
    <QuerySet [{'capacity': 10}, {'capacity': 20}, {'capacity': None}, {'capacity': None}, {'capacity': None}, {'capacity': None}, {'capacity': None}, {'capacity': None}, {'capacity': None}, {'capacity': None}]>
    """
    """ only print null values with desc order """
    # null_handling = Restuarants.objects.filter(capacity__isnull=False).order_by('-capacity').values('capacity')
    # print(null_handling)

    """ Coalesce(*expressions, **extra) 
    Accepts a list of at least two field names or expressions and returns the first non-null value 
    (note that an empty string is not considered a null value). Each argument must be of a similar type, 
    so mixing text and numbers will result in a database error.
    """
    from django.db.models.functions import Coalesce
    # print(
    #     # Restuarants.objects.aggregate(total_capacity=Sum('capacity')) # {'total_capacity': None}
    #     # Restuarants.objects.aggregate(total_capacity=Coalesce(Sum('capacity'), 0)) # {'total_capacity': 0}
    #     # """ Let's check for rating model """
    #     # Rating.objects.filter(rating__lt=0).aggregate(total_Avg_capacity=Avg('rating', default=0.0)) # {'total_Avg_capacity': None} using default output will be: {'total_Avg_capacity': 0.0}
    #     Rating.objects.filter(rating__lt=0).aggregate(total_Avg_capacity=Coalesce(Avg('rating'), 0.0)) # {'total_Avg_capacity': 0.0}
    # )
    """ Example of Coalesce () """
    # r = Restuarants.objects.first()
    # r.nickname = 'Arman'
    # r.save()
    # print(
    #     Restuarants.objects.annotate(
    #         name_value = Coalesce( F('nickname'), F('name') )     
    #     ).values('name_value')
    # )
    
    """ Conditional Expression (Case, When) in ORM """
    """ Case(*cases, **extra)
    A Case() expression is like the if … elif … else statement in Python. 
    Each condition in the provided When() objects is evaluated in order, 
    until one evaluates to a truthful value. The result expression from the 
    matching When() object is returned.
    """    
    """ When(condition=None, then=None, **lookups) 
    A When() object is used to encapsulate a condition and its result for use in the 
    conditional expression. Using a When() object is similar to using the filter() method. 
    The condition can be specified using field lookups, Q objects, or 
    Expression objects that have an output_field that is a BooleanField. 
    The result is provided using the then keyword
    """
    
    from django.db.models import Case, When, Value
    
    # italian = Restuarants.TypeChoices.ITALIAN
    # restuarant = Restuarants.objects.annotate(
    #     is_italian = Case(
    #         When(restuarant_type=italian, then=True),
    #         default=False
    #     )
    # )
    # print(
    #     restuarant.filter(is_italian=True)
    # )
    
    """ Lets see another example for sales model """
    # restuarant = Restuarants.objects.annotate(no_sales=Count('sales'))
    # restuarant = restuarant.annotate(
    #     is_popular = Case(
    #         When(no_sales__gt=8, then=True),
    #         default=False
    #     )
    # )
    # print(
    #     restuarant.values('no_sales', 'is_popular'), " \n\n No of Sales are greater then 8: ",
    #     restuarant.filter( is_popular=True)
    # )
    
    """ Example:
    1- restuarant has average rating > 3.5 and
    2- resruarant has more then 1 rating
    """
    """ 1- annotate resturarant with average rating and number of ratings """
    # restuarant = Restuarants.objects.annotate(
    #     average = Avg('ratings__rating'),
    #     no_ratings = Count('ratings__pk')
    # )
    # restuarant = restuarant.annotate(
    #     hight_rated = Case(
    #         When(average__gt=3.5, no_ratings__gt=1, then=True),
    #         default=False
    #     )
    # )
    # print(
    #     # restuarant.filter(hight_rated=True) # Output:<QuerySet [<Restuarants: Pizzeria 1>]>
    #     restuarant.filter(hight_rated=True).values('average', 'no_ratings') # Output: <QuerySet [{'average': 4.0, 'no_ratings': 4}]>
    #     )
    
    """ Uses Multiple When() """
    restuarant = Restuarants.objects.annotate(
        average = Avg('ratings__rating'),
        no_ratings = Count('ratings__pk')
    )
    restuarant = restuarant.annotate(
        Rated_list = Case(
            When(average__gt=3.5, then=Value("Highly Rated")),
            When(average__range=(2.5, 3.5), then=Value('Average Rated')),
            When(average__lt=2.0, then=Value('Bad Rating'))
        )
    )
    print(
        restuarant.filter(Rated_list='Average Rated')
    )