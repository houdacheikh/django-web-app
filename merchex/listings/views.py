from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band,contact;
from listings.models import listing;
def hello(request):
    bands = Band.objects.all()
    return render(request,
    'listings/hello.html',
    {'bands': bands})
def about(request):
    return HttpResponse('<h1>À propos</h1> <p>hi we are supporting gaza!</p>')
def list(request):
    annonces=listing.objects.all()
    return render(request,
    'listings/list.html',
    {'annonces': annonces})
def contactview(request):
   ctt=contact.objects.all()
   return render(request,
   'listings/mescts.html',
   {'ctt': ctt})