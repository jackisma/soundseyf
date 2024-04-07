from django.shortcuts import render
from .models import Post 
from django.views import generic
from django.utils import timezone



class PostList(generic.ListView):
    now = timezone.now()
    queryset = Post.objects.filter(status='p' , published_on__lte=now).order_by('-created_on')
    context_object_name = 'post_list'
    paginate_by = 3
    template_name = "blog/blog-home.html" 


class DetailView(generic.DetailView):
    model = Post 
    template_name = "blog/blog-single.html"
