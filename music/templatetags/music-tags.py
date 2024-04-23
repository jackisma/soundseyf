from django import template 
from music.models import *


register = template.Library()

@register.inclusion_tag('music/somepalos.html')
def somepalos():
    somepalos = Palo.objects.all().order_by('name')[:4]
    return  {"somepalos":somepalos}