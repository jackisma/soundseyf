from django.shortcuts import render
from .models import Composer, MasterPiece 
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Composers List View
def ComposersView(request):
    composers = Composer.objects.all()

    p = Paginator(composers,8)
    try:
        page_number = request.GET.get('page')
        composers = p.get_page(page_number)
    except EmptyPage:
        composers = composers.get_page(1)
    except PageNotAnInteger:
        composers = composers.get_page(1)

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
        # python valrus
        if s := request.GET.get('s'):
            composers = composers.filter(name__contains=s)

    context = {'composers' : composers}
    return render(request , 'music/composers.html' , context)   


