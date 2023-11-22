from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band,contact;
from listings.models import Annonce;
def band_list(request):
    bands = Band.objects.all()
    return render(request,
    'listings/band_list.html',
    {'bands': bands})
def about(request):
    return HttpResponse('<h1>À propos</h1> <p>hi we are supporting gaza!</p>')
def list_annonces(request):
    annonces=Annonce.objects.all()
    return render(request,
    'listings/list_annonces.html',
    {'annonces': annonces})
def contactview(request):
   ctt=contact.objects.all()
   return render(request,
   'listings/mescts.html',
   {'ctt': ctt})
def band_detail(request, band_id): 
   band=Band.objects.get(id=band_id)
   return render(request,
        'listings/band_detail.html',
        {'band': band})
def annonce_detail(request, ann_id): 
   annonce=Annonce.objects.get(id=ann_id)
   return render(request,
        'listings/annonce_detail.html',
        {'annonce': annonce})