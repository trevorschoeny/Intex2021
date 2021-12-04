from django.contrib import admin

from django.contrib import admin
from .models import PdPrescriber,  PdDrugs, PdPrescriberDrugs, PdStatedata, PdCredential, PdSpecialty, PdTriplenew

# Register your models here.
admin.site.register(PdDrugs)
admin.site.register(PdPrescriber)
admin.site.register(PdPrescriberDrugs)
admin.site.register(PdStatedata)
admin.site.register(PdCredential)
admin.site.register(PdSpecialty)
admin.site.register(PdTriplenew)