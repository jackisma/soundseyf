from django.urls import path 
from .views import * 

app_name = "music"

urlpatterns = [
   path('composers',ComposersView , name="composers" ),
]