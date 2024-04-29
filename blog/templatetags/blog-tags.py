from django import template 
from blog.models import Post
register = template.Library()


@register.inclusion_tag('blog/recentposts.html')
def recentpost():
    recentposts = Post.objects.all().order_by('published_on')[:3]
    return  {"recentposts":recentposts}


@register.inclusion_tag('blog/sidebar.html')
def popularpost():
    popularposts = Post.objects.all().order_by('-counted_views')[:3]
    return  {"popularposts":popularposts}