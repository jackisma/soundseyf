from django.shortcuts import render
from music.models import * 

def index_view(request):
    pieces = MasterPiece.objects.all()
    context = {"pieces" : pieces}
    return render (request , 'website/index.html',context)



def contact_view(request):
    return render (request , 'website/contact.html')



def about_view(request):
    return render (request , 'website/about.html')
