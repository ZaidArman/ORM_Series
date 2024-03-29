# Generated by Django 5.0.2 on 2024-03-13 11:31

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rating_rating_value_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restuarants',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[core.models.restuarant_name_begin_with_a]),
        ),
        migrations.AddConstraint(
            model_name='restuarants',
            constraint=models.CheckConstraint(check=models.Q(('latitude__gte', -90), ('latitude__lte', 90)), name='latitude_valid', violation_error_message='Latitude invalid, must be fall between -90 to +90'),
        ),
        migrations.AddConstraint(
            model_name='restuarants',
            constraint=models.CheckConstraint(check=models.Q(('longitude__gte', -180), ('longitude__lte', 180)), name='longitude_valid', violation_error_message='longitude invalid, must be fall between -90 to +90'),
        ),
    ]
