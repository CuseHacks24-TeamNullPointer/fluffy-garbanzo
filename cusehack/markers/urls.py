from django.urls import path
#from django.views.generic import TemplateView
from markers.views import MapView
urlpatterns = [
    path(
        "map/",
        MapView.as_view()
        #TemplateView.as_view(template_name="map.html"),
    ),
]
