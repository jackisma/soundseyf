from django.urls import path 
from .views import * 

app_name = "music"

urlpatterns = [
   path('composers',ComposersView , name="composers" ),
   path('pieces/<int:cid>' , ComposerPieces , name="pieces"),
   path('search/',composer_search,name='search'),
]