from django import forms 
from Boxeo.models import Boxeador
from Boxeo.models import Torneo
from Boxeo.models import Team

class FormBoxeador(forms.ModelForm):
    class Meta:
        model = Boxeador
        fields = '__all__'

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    peso = forms.FloatField()
    cinturones = forms.IntegerField()
    ko = forms.IntegerField()


class FormTorneo(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = '__all__'
    
    nombre = forms.CharField(max_length=50)
    ubicacion = forms.CharField(max_length=50)
    cupos = forms.IntegerField()
    categoria = forms.CharField(max_length=20)
    fecha = forms.DateField()
    inscripcion = forms.CharField(max_length=20)

class FormTeam(forms.ModelForm):
    class Meta:
        model = Team  
        fields = '__all__'
    
    nombre = forms.CharField(max_length=50)
    nacionalidad = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=20)
    titulos = forms.IntegerField()
    entrenador = forms.CharField(max_length=60)
    lesionados = forms.CharField(max_length=15)
