import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Restuarants, Rating, Sales


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        # get or create an admin user
        user = User.objects.filter(username='admin')
        if not user.exists():
            user = User.objects.create_superuser(username='admin', password='admin')
        else:
            user = user.first()

        restaurants = [
            {'name': 'Pizzeria 1', 'date_opened': timezone.now() - timezone.timedelta(days=20), 'restuarant_type': Restuarants.TypeChoices.ITALIAN, 'latitude': 55.869829854, 'longitude': -4.28583219},
            {'name': 'Pizzeria 2', 'date_opened': timezone.now() - timezone.timedelta(days=27), 'restuarant_type': Restuarants.TypeChoices.ITALIAN, 'latitude': 55.862, 'longitude': -4.247},
            {'name': 'Golden Dragon', 'date_opened': timezone.now() - timezone.timedelta(days=15), 'restuarant_type': Restuarants.TypeChoices.CHINESE, 'latitude': 55.953251, 'longitude':  -3.188267},
            {'name': 'Bombay Bustle', 'date_opened': timezone.now() - timezone.timedelta(days=44), 'restuarant_type': Restuarants.TypeChoices.INDIAN, 'latitude': 51.509865, 'longitude':  -0.118092},
            {'name': 'Chinese 2', 'date_opened': timezone.now() - timezone.timedelta(days=31), 'restuarant_type': Restuarants.TypeChoices.CHINESE, 'latitude': 53.400002, 'longitude':  -2.983333},
            {'name': 'Chinese 3', 'date_opened': timezone.now() - timezone.timedelta(days=71), 'restuarant_type': Restuarants.TypeChoices.CHINESE, 'latitude': 55.070859, 'longitude':  -3.60512},
            {'name': 'Indian 2', 'date_opened': timezone.now() - timezone.timedelta(days=46), 'restuarant_type': Restuarants.TypeChoices.INDIAN, 'latitude': 53.350140, 'longitude':  -6.266155},
            {'name': 'Pizzeria 3', 'date_opened': timezone.now() - timezone.timedelta(days=4), 'restuarant_type': Restuarants.TypeChoices.ITALIAN, 'latitude': 54.966667, 'longitude':  -1.600000},
            {'name': 'Pizzeria 4', 'date_opened': timezone.now() - timezone.timedelta(days=61), 'restuarant_type': Restuarants.TypeChoices.ITALIAN, 'latitude': 48.856614, 'longitude':  2.3522219},
            {'name': 'Italian 1', 'date_opened': timezone.now() - timezone.timedelta(days=37), 'restuarant_type': Restuarants.TypeChoices.ITALIAN, 'latitude': 41.902782, 'longitude':  12.496366},
        ]

        Restuarants.objects.all().delete()
        for r in restaurants:
            Restuarants.objects.create(**r)

        restuarant = Restuarants.objects.all()

        # create some ratings
        for _ in range(30):
            Rating.objects.create(
                restuarant=random.choice(restuarant),
                user=user,
                rating=random.randint(1,5)
            )

        # create some sales
        for _ in range(100):
            Sales.objects.create(
                restuarant=random.choice(restuarant),
                income=random.uniform(5, 100),
                datetime=timezone.now() - timezone.timedelta(days=random.randint(1,50))
            )