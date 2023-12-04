from ast import Delete
from django import views
from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.models import Band;
from django.core.mail import send_mail
from listings.models import Annonce;
from listings.forms import BandForm,ContactUsForm,AnnForm;
def band_list(request):
    bands = Band.objects.all()
    return render(request,
    'listings/band_list.html',
    {'bands': bands})
def invalide(request):
    return render(request,
    'listings/invalidedata.html')
def about(request):
    return render(request,
    'listings/about_us.html')
def list_annonces(request):
    annonces=Annonce.objects.all()
    return render(request,
    'listings/list_annonces.html',
    {'annonces': annonces})
from django.core.mail import send_mail
...

def contactview(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('email-sent')
        else:
            return redirect('donnes_invalides')
    else:
     form = ContactUsForm()
    return render(request,
        'listings/mescts.html',
        {'form': form})
def email_redirect(request):
    return render(request,
    'listings/contact.html')
def band_detail(request, band_id): 
   band1=Band.objects.get(id=band_id)
   return render(request,
        'listings/band_detail.html',
        {'band': band1},)
def band_annonces(request,band_id):
     band1=Band.objects.get(id=band_id)
     anns=Annonce.objects.filter(band=band1)
     return render(request,
        'listings/band_annonces.html',
        {'anns': anns},)
def annonce_detail(request, ann_id): 
   annonce=Annonce.objects.get(id=ann_id)
   return render(request,
        'listings/annonce_detail.html',
        {'annonce': annonce})
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('trajet', band.id)
    else:
        form = BandForm()
    return render(request,
            'listings/band_create.html',
            {'form': form})
def ann_create(request):
    if request.method == 'POST':
        form = AnnForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('trajet3', band.id)
    else:
        form = AnnForm()
    return render(request,
            'listings/annonce_create.html',
            {'form': form})
def band_change(request, band_id):
    band=Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST,instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('trajet', band.id)
    else:
        form = BandForm(instance=band)
    return render(request,
            'listings/band_change.html',
            {'form': form})
def annonce_change(request, ann_id):
    band=Annonce.objects.get(id=ann_id)
    if request.method == 'POST':
        form = AnnForm(request.POST,instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('trajet3', band.id)
    else:
        form = AnnForm(instance=band)
    return render(request,
            'listings/band_change.html',
            {'form': form})
def band_delete(request, band_id):
    band=Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-deleted')
    return render(request,
            'listings/delete-band.html',
            {'band': band})
def deleted_band(request) :
     return render(request,
            'listings/deleted_band.html')
def deleted_annonce(request) :
     return render(request,
            'listings/deleted_annonce.html')
def annonce_delete_redirect(request,ann_id):
    ann=Annonce.objects.get(id=ann_id)
    if request.method == 'POST':
        form = AnnForm(instance=ann)
        ann.delete() 
        return redirect('annonce-deleted')   
    else :
        form = AnnForm(instance=ann)    
    return render(request,
            'listings/annonce-delete-redirect.html',
            {'form': form})
def delete_annonce(request, ann_id):
    ann=Annonce.objects.get(id=ann_id)
    if request.method == 'POST':
        form = AnnForm(instance=ann)
        return redirect('annonce-delete-redirect', ann_id)
    else:
        form = AnnForm(instance=ann)
    return render(request,
            'listings/delete-annonce.html',
            {'form': form})
        

