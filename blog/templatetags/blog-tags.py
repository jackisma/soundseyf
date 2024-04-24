from django import template 
from blog.models import Post
register = template.Library()


@register.inclusion_tag('blog/recentposts.html')
def recentpost():
    recentposts = Post.objects.all().order_by('published_on')[:3]
    return  {"recentposts":recentposts}