from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render (request , 'website/index.html')


def contact_view(request):
    return render (request , 'website/contact.html')