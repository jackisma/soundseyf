from django.shortcuts import render
from .models import Composer 



def ComposersView(request):
    composers = Composer.objects.all()
    context = {"composers": composers}
    return render(request,'music/composers.html',context)