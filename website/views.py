from django.shortcuts import render
from music.models import * 


# Home index view Function
def index_view(request):
    pieces = MasterPiece.objects.all()
    context = {"pieces" : pieces}
    return render (request , 'website/index.html',context)


# Contact view Function
def contact_view(request):
    return render (request , 'website/contact.html')


# About view Function
def about_view(request):
    return render (request , 'website/about.html')
