from django.shortcuts import render
from django.core.serializers import serialize
from django.contrib.gis.serializers import geojson
import json


from django.contrib.gis.geos import Point
from django.db.models import F, Func
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import GEOSGeometry
from .models import DataGoaWgs84

class PointFromLatLon(Func):
    function = 'ST_Point'
    template = '%(function)s(%(expressions)s)'
    output_field = PointField(srid=4326)

# Create your views here.
def guamap(request):
    title = "Map Goa"


    qs = DataGoaWgs84.objects.annotate(
        point=PointFromLatLon(F('longitude'), F('latitude'))
    )

    features = []
    for obj in qs:
        features.append({
            "type": "Feature",
            "geometry": json.loads(obj.point.geojson),
            "properties": {
                "kode_desa": obj.kode_desa,
                "kecamatan": obj.kecamatan,
                "nama_objek": obj.nama_objek,
                # "kode_karts": obj.kode_karts,
                # "nama_objek": obj.nama_objek,
                # "jenis": obj.jenis,
                # "x": obj.x,
                # "y": obj.y,
                # "z": obj.z,
                # "provinsi": obj.provinsi,
                # "kabupaten": obj.kabupaten,
                # "kecamatan": obj.kecamatan,
                # "desa": obj.desa,
                # "dukuh": obj.dukuh,
                # "tempat_unik": obj.tempat_unik,
                # "letak": obj.letak,
                # "akses": obj.akses,
                # "biota": obj.biota,
                # "potensi": obj.potensi,
                # "pemanfaatan": obj.pemanfaatan,
                # "keterangan": obj.keterangan,
            }
        })

    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }
    print (geojson_data)
    context = {
        'title': title,
        'geojson_data': geojson_data
    }
    
    return render(request, "goa/goa copy.html", context)