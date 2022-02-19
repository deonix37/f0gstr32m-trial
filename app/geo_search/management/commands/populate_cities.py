import argparse
import csv

from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from geo_search.models import City


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        with options['csv_file'] as csv_file:
            City.objects.bulk_create(
                (City(**row) for row in self.get_city_rows(csv_file))
            )

    def get_city_rows(self, csv_file):
        for row in csv.DictReader(csv_file):
            row['location'] = Point(
                float(row.pop('geo_lon')),
                float(row.pop('geo_lat')),
            )
            yield row
