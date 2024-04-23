from pickle import NONE
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.urls import reverse

# Composers List View
def ComposersView(request):
    composers = Composer.objects.all()
    p = Paginator(composers,10)
    try:
        page_number = request.GET.get('page')
        composers = p.get_page(page_number)
    except EmptyPage:
        composers = composers.get_page(1)
    except PageNotAnInteger:
        composers = composers.get_page(1)
    if request.user.is_authenticated:
         favorited_composer_ids = set(request.user.favoritecomposer_set.values_list('composer__id', flat=True))
         context = {"composers": composers, "favorited_composer_ids": favorited_composer_ids}
         return render(request,'music/composers.html',context)

    else:
         context = {"composers": composers}
         return render(request,'music/composers.html',context)



# Composers Pieces List View
def ComposerPieces(request,cid):
    all_composers = Composer.objects.all()
    current_composer = get_object_or_404(all_composers , pk = cid) 
    pieces = MasterPiece.objects.filter(composer = cid)
    p = Paginator(pieces,5)
    try:
        page_number = request.GET.get('page')
        pieces = p.get_page(page_number)
    except EmptyPage:
        pieces = pieces.get_page(1)
    except PageNotAnInteger:
        pieces = pieces.get_page(1)
    context = {"composer" : current_composer , "pieces" : pieces }
    return render (request,'music/masterpieces.html',context)








# search view For Home index That User can Search and find a specifc Composer 
def composer_search(request):
    composers = Composer.objects.all()
    
    if request.method == 'GET':
        search_query = request.GET.get('s', '')
        if search_query:
            composers = composers.filter(name__icontains=search_query)
            context = {'composers': composers}
            if request.user.is_authenticated:
                favorited_composer_ids = set(request.user.favoritecomposer_set.values_list('composer__id', flat=True))
                context = {"composers": composers, "favorited_composer_ids": favorited_composer_ids}
                return render(request,'music/composers.html',context)
            else:
                return render(request, 'music/composers.html', context)

    return redirect(request.META.get('HTTP_REFERER', 'music:composers'))





@login_required
def favorite_composer(request, composer_id):
    composer = get_object_or_404(Composer, pk=composer_id)
    favorite, created = FavoriteComposer.objects.get_or_create(user=request.user, composer=composer)
    if not created:
        favorite.delete()  # Remove the composer from favorites if it's already favorited
    # Redirect back to the same page where the action was initiated
    return redirect(request.META.get('HTTP_REFERER', 'music:composers'))




@login_required
def FavoritesView(request):
    # Retrieve liked composers associated with the current user
    liked_composers = Composer.objects.filter(favoritecomposer__user=request.user)
    # Render the favorites.html template with the liked composers
    return render(request, 'music/favorites.html', {'liked_composers': liked_composers})




@login_required
def PaloView(request):
    palos = Palo.objects.all()
    context = {"palos" : palos}
    return render (request, 'music/palos.html' , context)