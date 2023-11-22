from django.contrib import admin
from listings.models import Band
from listings.models import Annonce
from listings.models import contact
class BandAdmin(admin.ModelAdmin):  
 list_display = ('name', 'year_formed', 'genre')
admin.site.register(Band, BandAdmin)
class listAdmin(admin.ModelAdmin):  
 list_display = ('title', 'description', 'type', 'band')
admin.site.register(Annonce, listAdmin) 
class contactAdmin(admin.ModelAdmin):  
 list_display = ('email', 'number')
admin.site.register(contact, contactAdmin)
