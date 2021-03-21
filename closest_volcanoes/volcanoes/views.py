from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Volcanoe
from django.contrib.gis.gdal import SpatialReference, CoordTransform


longitude = -5.91251
latitude = 54.60719

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Volcanoe
    context_object_name = 'volcanoes'
    queryset = Volcanoe.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'index.html'

home = Home.as_view()