from django.shortcuts import redirect, render
from music.models import * 
from .forms import * 
import sweetify

# Home index view Function
def index_view(request):
    pieces = MasterPiece.objects.all()
    context = {"pieces" : pieces}
    return render (request , 'website/index.html',context)


# Contact view Function
def contact_view(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         form.save()       
         sweetify.success(request,'your message has been sent',persistent = 'OK')
      else:
         sweetify.error(request,'your ticket doesn\'t  post',persistent = ':(')

      
   form = ContactForm(request.POST)
   context = {'form': form}
   return render(request , 'website/contact.html',context)






# About view Function
def about_view(request):
    return render (request , 'website/about.html')





def subscribe_view(request):
    if request.method == 'POST':
         form = SubscribeForm(request.POST)
         if form.is_valid():
            form.save()       
            sweetify.success(request,'Welcome to our community! Thank you for supporting',persistent = 'OK')
         else:
            sweetify.error(request,'an error occured',persistent = ':(')

      
    form = SubscribeForm(request.POST)
    context = {'form': form}
    return render(request , 'website/index.html',context)