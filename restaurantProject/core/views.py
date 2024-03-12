from django.shortcuts import render, redirect
from .forms import restuarantForm
from .models import Restuarants, Rating, Sales, StaffRestuarant, Product, Order
from django.db.models import Sum, Prefetch
from django.db import transaction
from django.utils import timezone
import sys
from functools import partial # use to send email manually for testing

# calling the form
from core.forms import ProductOrderForm
# Create your views here.

def index(request):
# SQL Query Optimization using prefetch_related():
    """
        prefetch_related(lookups)
        Returns a QuerySet that will automatically retrieve, in a single batch, related objects for each of the specified lookups.
        This has a similar purpose to select_related, in that both are designed to stop the deluge of database queries that is caused by accessing related objects, but the strategy is quite different.
        select_related works by creating an SQL join and including the fields of the related object in the SELECT statement. For this reason, select_related gets the related objects in the same database query. However, to avoid the much larger result set that would result from joining across a ‘many’ relationship, select_related is limited to single-valued relationships - foreign key and one-to-one.
        prefetch_related, on the other hand, does a separate lookup for each relationship, and does the ‘joining’ in Python. This allows it to prefetch many-to-many, many-to-one, and GenericRelation objects which cannot be done using select_related, in addition to the foreign key and one-to-one relationships that are supported by select_related. It also supports prefetching of GenericForeignKey, however, it must be restricted to a homogeneous set of results. For example, prefetching objects referenced by a GenericForeignKey is only supported if the query is restricted to one ContentType.
    """
    # restuarant = Restuarants.objects.prefetch_related('ratings', 'sales') 
    # restuarant = Restuarants.objects.filter(name__istartswith='c').prefetch_related('ratings', 'sales')
    # context = {'restuarant': restuarant}
    # return render(request, 'index.html', context)
    
# SQL Query Optimization using Select_prefetch():  Returns a QuerySet that will “follow” foreign-key relationships, selecting additional related-object data when it executes its query. This is a performance booster which results in a single more complex query but means later use of foreign-key relationships won’t require database queries.
    # ratings = Rating.objects.select_related('restuarant')
    # context = {'ratings':ratings }
    # return render(request, 'index.html', context)

# SQL Query Optimization using only(): The only() method is essentially the opposite of defer(). Only the fields passed into this method and that are not already specified as deferred are loaded immediately when the queryset is evaluated. If you have a model where almost all the fields need to be deferred, using only() to specify the complementary set of fields can result in simpler code.
    # ratings = Rating.objects.only('rating', 'restuarant__name').select_related('restuarant')
    # context = {'ratings':ratings }
    # return render(request, 'index.html', context)

# get all 5 start ratings,  and fetch the sales for all the restuarants with 5-start ratings
    # restuarant = Restuarants.objects.prefetch_related('ratings', 'sales') \
    #         .filter(ratings__rating=5) \
    #         .annotate(total=Sum('sales__income')) # annotate() used for grouped_by any objects
    # print(restuarant)
    # return render(request, 'index.html')
    
    # get all 5 start ratings,  and fetch the sales for all the restuarants with 5-start ratings - 
    # using pre_fetch() object: 
    """
        Syntaxt:- class Prefetch(lookup, queryset=None, to_attr=None)
        The Prefetch() object can be used to control the operation of prefetch_related().
        The lookup argument describes the relations to follow and works the same as the string based lookups passed to prefetch_related()
    """
    # month_ago = timezone.now() - timezone.timedelta(days=30)
    # monthly_sales = Prefetch(
    #     'sales',
    #     queryset=Sales.objects.filter(datetime__gte=month_ago)
    # )
    # restuarant = Restuarants.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating=5)
    # restuarant = restuarant.annotate(total=Sum('sales__income')).order_by('total')
    # print( [r.total for r in restuarant] )
    # context = {'restuarant':restuarant}
    # return render(request, 'index.html', context) 

    # if request.method == 'POST':
    #     form = restuarantForm(request.POST or None)
    #     if form.is_valid():
    #         # form.save()
    #         print(form.cleaned_data)
    #     else:
    #         return render(request, 'index.html', {'form': form})
    # context = {'form': restuarantForm()}
    # return render(request, 'index.html', context)
    
# here we use to check the prefetch_related() for query opt
    # jobs = StaffRestuarant.objects.all() # this query will output about 21 query, which is high
    jobs = StaffRestuarant.objects.prefetch_related('restuarant', 'staff') # only 3 query
    for j in jobs:
        print(j.restuarant.name)
        print(j.staff.staff_name)
    return render(request, 'index.html') 


""" testing email function to test our commit """
def User_Welcome_Email(email):
    print(f" Dear {email}, Thank You for Your Order! ")

def ProductOrderView(request):
    if request.method == 'POST':
        form = ProductOrderForm(request.POST)
        if form.is_valid():
            
            with transaction.atomic():
                """ To solve the concurrent problem , we use select_for_update() 
                
                select_for_update(nowait=False, skip_locked=False, of=(), no_key=False)
                Returns a queryset that will lock rows until the end of the transaction, 
                generating a SELECT ... FOR UPDATE SQL statement on supported databases.
                """
                product = Product.objects.select_for_update().get(
                    id=form.cleaned_data['product_order'].pk
                )
                
                order = form.save()
                # """
                # if we save the form and the system crash the below code will not execute and 
                # db will not be update, for that purpose we use ATOMICITY / Transactions
                # """

                # sys.exit(1) # Testing: if system crash it will rollback the db
                order.product_order.number_in_stock -= order.number_of_items 
                order.product_order.save() #product_order is the ForeignKey of Order table
            transaction.on_commit(partial(User_Welcome_Email, "zaidtesting@test.com")) # To test either our commit work or not
            
            return redirect('product_order')
        else:
            context = {'form': form}
            return render(request, 'order.html', context)
            
    form = ProductOrderForm()
    context = {'form': form}
    return render(request, 'order.html', context)