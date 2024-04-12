from typing import Any
from django.shortcuts import render
from .models import Post 
from django.views import generic
from django.utils import timezone

# Blog Home Post's List View Class Created by Django's Listview
class PostList(generic.ListView):
    now = timezone.now()
    queryset = Post.objects.filter(status='p' , published_on__lte=now).order_by('-created_on')
    context_object_name = 'post_list'
    paginate_by = 3
    template_name = "blog/blog-home.html" 



# Blog Single View Class Created by Django's Detailview
class DetailView(generic.DetailView):
    model = Post 
    template_name = "blog/blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        # Get The previous post 
        previous_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
        # Get the next post 
        next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
        context['previous_post'] = previous_post 
        context['next_post'] = next_post 
        return context 
    