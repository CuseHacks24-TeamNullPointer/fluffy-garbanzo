from django.contrib.gis import admin

# Register your models here.
from markers.models import Marker


@admin.register(Marker)
class MarkerAdmin(admin.GISModelAdmin):
    list_display = ("name", "location")
