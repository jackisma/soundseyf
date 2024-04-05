from django.shortcuts import render
from .models import Post 
from django.views import generic

class PostList(generic.ListView):
    queryset = Post.objects.filter(status='p').order_by('-created_on')
    template_name = "blog/blog-home.html" 

class DetailView(generic.DetailView):
    model = Post 
    template_name = "blog/blog-single.html"
