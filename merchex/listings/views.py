from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')
def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
def list(request):
    return HttpResponse('<h1>Voici la liste des annonces</h1> <p>Nous adorons palestine</p>')
def contact(request):
    return HttpResponse('<h1>Contact us</h1> <p>i love palestine !</p>')

