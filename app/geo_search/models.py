from django.contrib.gis.db.models import PointField
from django.db import models


class City(models.Model):
    address = models.CharField(max_length=255, unique=True)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    federal_district = models.CharField(max_length=255)
    region_type = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    area_type = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    city_type = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    settlement_type = models.CharField(max_length=255)
    settlement = models.CharField(max_length=255)
    kladr_id = models.CharField(max_length=255)
    fias_id = models.CharField(max_length=255)
    fias_level = models.CharField(max_length=255)
    capital_marker = models.CharField(max_length=255)
    okato = models.CharField(max_length=255)
    oktmo = models.CharField(max_length=255)
    tax_office = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)
    population = models.CharField(max_length=255)
    foundation_year = models.CharField(max_length=255)
    location = PointField(unique=True)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.address
