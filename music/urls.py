from django.urls import path 
from .views import * 

app_name = "music"

urlpatterns = [
   path('composers',ComposersView , name="composers" ),
   path('pieces/<int:cid>' , ComposerPieces , name="pieces"),
   path('search/',composer_search,name='search'),
   path('favorite/<int:composer_id>/', favorite_composer, name='Favorites'),
   path('favorites/', FavoritesView, name='Likes'),


]