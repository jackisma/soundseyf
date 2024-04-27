from atexit import register
from django import template 
from music.models import Composer

register = template.Library()


@register.inclusion_tag('website/somecomposers.html')
def somegeniuses():
    composers = Composer.objects.all()[:8]
    return {"composers":composers}
