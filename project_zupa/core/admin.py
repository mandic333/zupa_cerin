from django.contrib import admin

from . import models
from . import forms

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

# Register your models here.
admin.site.register(models.Glasnik)
admin.site.register(models.Rental)
admin.site.register(models.Post)


    
