from django.contrib import admin
from app.sie.models import *
# Register your models here.

class ProspectoConfig(admin.ModelAdmin):
    list_display = ["p_padre","p_alumno"]

admin.site.register(Empresa)
admin.site.register(Nivel)
admin.site.register(Grado)
admin.site.register(Prospecto,ProspectoConfig)