from django.shortcuts import render, redirect
from .models import Mural
import os
import folium
import base64
from folium import IFrame

# Create your views here.
def home(request):
    # objects
    murals = Mural.objects.all()

    # folium
    map_graph = folium.Map(location=[52.145259, 21.051619], zoom_start=13)
    m = map_graph
    folium.LayerControl().add_to(m)

    for mural in murals:
        coordinates = (mural.lat, mural.lon)
        tooltip = mural.title
        popup = mural.photo

        # encoded = base64.b64encode(open(mural.photo, 'rb').read())
        # html = '<img src="data:image/png;base64,{}">'.format
        # iframe = IFrame(html(encoded.decode('UTF-8')), width=400, height=350)
        # popup = folium.Popup(iframe, max_width=400)

        folium.Marker(location=coordinates,
                      tooltip=tooltip,
                      popup=popup).add_to(m)

    ## adding to view

    # folium.Marker(location=[52.1614339, 21.0267905],
    #               tooltip='<b>Stackoverflow</b><br><br>2021.01.01').add_to(m)
    # folium.Marker(location=[52.1419292, 21.0549329]).add_to(m)

    ## exporting
    m = m._repr_html_()
    context = {'my_map': m}

    ## rendering
    return render(request, 'geoApp/home.html', context)
