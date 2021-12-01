from django.contrib import admin

from django.contrib import admin
from .models import PdPrescriber,  PdDrugs, PdStatedata, PdTriple

# Register your models here.
admin.site.register(PdDrugs)
admin.site.register(PdPrescriber)
admin.site.register(PdStatedata)
admin.site.register(PdTriple)