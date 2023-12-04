
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list,name='trajet2'),
    path('bands/<int:band_id>/', views.band_detail, name='trajet'),
    path('annonces/', views.list_annonces,name='trajet4'),
    path('detail_annonce/<int:ann_id>/', views.annonce_detail,name='trajet3'),
    path('contact-us/', views.contactview,name='retour'),
    path('band-annonces/<int:band_id>/', views.band_annonces,name='trajet5'),
    path('email-sent', views.email_redirect,name='email-sent'),
    path('donnes_invalides', views.invalide,name='donnes_invalides'),
    path('about-us', views.about,name='about-us'),
    path('bands/add/', views.band_create, name='band-create'),
    path('annonces/add/', views.ann_create, name='annonce-create'),
    path('bands/<int:band_id>/change/', views.band_change, name='band-change'),
    path('annonces/<int:ann_id>/change/', views.annonce_change, name='annonce-change'),
    path('band/<int:band_id>/delete-band/', views.band_delete, name='band-delete'),
    path('annonce/deleted', views.deleted_annonce, name='annonce-deleted'),
    path('band/deleted', views.deleted_band, name='band-deleted'),
    path('annonce/<int:ann_id>/delete-annonce/', views.delete_annonce, name='delete-annonce'),
    path('annonce/<int:ann_id>/annonce-delete-redirect/', views.annonce_delete_redirect, name='annonce-delete-redirect'),

]