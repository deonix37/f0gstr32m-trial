from dadata import Dadata
from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.http import JsonResponse
from django.views import generic
from httpx import HTTPStatusError

from .models import City


class IndexView(generic.TemplateView):
    template_name = 'geo_search/index.html'


class AjaxCitiesView(generic.View):
    def get(self, request, *args, **kwargs):
        try:
            address = request.GET['address']
        except KeyError:
            return JsonResponse({}, status=400)

        try:
            radius = int(request.GET['radius'])
        except (KeyError, ValueError):
            radius = None

        search_location = None
        nearby_locations = []

        with Dadata(
            settings.DADATA_API_KEY,
            settings.DADATA_API_SECRET,
        ) as dadata:
            try:
                address_response = dadata.clean('address', address)
            except HTTPStatusError as e:
                return JsonResponse(e.response.json(), status=403)

        if address_response['result']:
            search_point = Point(
                float(address_response['geo_lon']),
                float(address_response['geo_lat']),
            )
            search_location = {
                'lng': search_point.x,
                'lat': search_point.y,
            }

            if radius is not None:
                nearby_points = City.objects.filter(
                    location__distance_lte=(search_point, D(km=radius)),
                ).exclude(
                    location=search_point,
                ).values_list('location', flat=True)
                nearby_locations = [{
                    'lng': point.x,
                    'lat': point.y,
                } for point in nearby_points]

        return JsonResponse({
            'searchLocation': search_location,
            'nearbyLocations': nearby_locations,
        })
