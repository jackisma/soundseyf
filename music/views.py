from django.shortcuts import render
from .models import Composer, MasterPiece 
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



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




def ComposerPieces(request,cid):
    all_composers = Composer.objects.all()
    current_composer = get_object_or_404(all_composers , pk = cid) 
    pieces = MasterPiece.objects.filter(composer = cid)
    p = Paginator(pieces,10)
    try:
        page_number = request.GET.get('page')
        pieces = p.get_page(page_number)
    except EmptyPage:
        pieces = pieces.get_page(1)
    except PageNotAnInteger:
        pieces = pieces.get_page(1)
    context = {"composer" : current_composer , "pieces" : pieces }
    return render (request,'music/masterpieces.html',context)


