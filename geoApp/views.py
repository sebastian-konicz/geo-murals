from django.shortcuts import render, redirect
from .models import Mural
import os
import folium

# Create your views here.
def home(request):
    # objects
    Mural.objects.all()

    # folium
    map_graph = folium.Map([52.145259, 21.051619], zoom_start=13)
    m = map_graph
    folium.LayerControl().add_to(m)


    ## exporting
    m = m._repr_html_()
    context = {'my_map': m}
    return render(request, 'geoApp/home.html', context)
