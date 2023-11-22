
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list,name='trajet2'),
    path('bands/<int:band_id>/', views.band_detail, name='trajet'),
    path('about-us/', views.about),
    path('annonces/', views.list_annonces,name='trajet4'),
    path('detail_annonce/<int:ann_id>/', views.annonce_detail,name='trajet3'),
    path('contact-us/', views.contactview),

]
