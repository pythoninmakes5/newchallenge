from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Text
# Create your views here.


def demo(request):
    obj=Place.objects.all()
    res=Text.objects.all()
    return render(request,"index.html",{'result':obj,'res':res})

