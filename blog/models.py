from pyexpat import model
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse



# Defining some Status choices for Status Field that is Placed in Post table
STATUS_CHOICES = {
    "d" : "Draft" , 
    "p" : "Published",
    "w" : "Withdrawn",
}

# Post Model Table For blog -- CONTAINS META DATA CLASS 
class Post(models.Model):
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(null=True)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)
    counted_views = models.IntegerField(default=0)
    login_required = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}'.format(self.title)
    


    def get_absolute_url(self):
        return reverse('blog:blog-single',kwargs={'slug':self.slug})