from django.shortcuts import render, redirect, get_object_or_404
from .models import Mural
import os
import folium
import base64
from folium import IFrame

# Create your views here.
# rendering map
def home(request):
    # filtrowanie po obszarze

    # objects
    murals = Mural.objects.all()

    # folium
    map = folium.Map(location=[52.145259, 21.051619], zoom_start=13, height='100%')

    folium.LayerControl().add_to(map)

    # making map fit whole visible screen
    # f = folium.Figure(height="100%")
    # m.add(f)

    for mural in murals:
        # variables from mural object
        coordinates = (mural.lat, mural.lon)
        tooltip = mural.title
        photo_url = mural.photo.url

        html = f'<div id="popup"><img calss="img-responsive" src="{photo_url}"></div>'

        popup = folium.Popup(html=html, max_width=400)

        popup_style = """
            #popup {
                max-width: 200px;
                max-height: 200px;
                overflow: hidden;
                }
            #popup img { 
                width: 100%;
                height: auto;
                }
            """

        # marker icon
        # icon = folium.Icon(color="red", icon='brush', prefix='fa')
        icon = folium.Icon(icon='glyphicon-picture')

        # adding to view
        folium.Marker(location=coordinates,
                      tooltip=tooltip,
                      popup=popup,
                      icon=icon).add_to(map)

    ## exporting
    # making map able to render
    map = map._repr_html_()
    # ? sending data to home page?
    context = {'mural_map': map, 'murals': murals}

    ## rendering
    return render(request, 'geoApp/home.html', context)

def mural_detail(request, pk):
    mural = get_object_or_404(Mural, pk=pk)
    return render(request, 'geoApp/mural_detail.html', {'mural': mural})

# encoded = base64.b64encode(open(mural.photo, 'rb').read())
# html = '<img src="data:image/png;base64,{}">'.format
# iframe = IFrame(html(encoded.decode('UTF-8')), width=400, height=350)

# height = "300"
# width = "400"