from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band;
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
def contact(request):
    return HttpResponse('<h1>Contact us</h1> <p>i love palestine !</p>')

