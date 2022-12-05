from django.contrib import admin
from Boxeo.models import Boxeador,Torneo,Team

# Register your models here.
class BoxeadorAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','edad','peso','cinturones','ko']

admin.site.register(Boxeador, BoxeadorAdmin)

class TorneoAdmin(admin.ModelAdmin):
    list_display = ['nombre','ubicacion','cupos','categoria','fecha','inscripcion']

admin.site.register(Torneo, TorneoAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['nombre','nacionalidad','categoria','titulos','entrenador','lesionados']

admin.site.register(Team, TeamAdmin)