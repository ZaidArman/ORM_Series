# Generated by Django 5.0.2 on 2024-03-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_restuarants_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='restuarants',
            name='nickname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]