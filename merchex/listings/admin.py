from django.contrib import admin
from listings.models import Band
from listings.models import listing
class BandAdmin(admin.ModelAdmin):  
 list_display = ('name', 'year_formed', 'genre')
admin.site.register(Band, BandAdmin)
class BandAd(admin.ModelAdmin):  
 list_display = ('title', 'description', 'type')
admin.site.register(listing, BandAd) 