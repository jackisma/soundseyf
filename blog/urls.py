from . import views 
from django.urls import path 

app_name = "blog"

urlpatterns = [
    path('',views.PostList.as_view(),name="blog-home"),
    path('<slug:slug>',views.DetailView.as_view(),name="blog-single"),
]