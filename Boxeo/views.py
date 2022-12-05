from django.shortcuts import render,redirect
from Boxeo.forms import FormBoxeador
from Boxeo.forms import FormTorneo
from Boxeo.forms import FormTeam
from Boxeo.models import Boxeador
from Boxeo.models import Torneo
from Boxeo.models import Team




def index(request):
    return render(request, 'Boxeo/index.html')

    
      
      
      
      
        #BOXEADORES
def listadoBoxeadores(request):
    boxeadores = Boxeador.objects.all()
    data = {'boxeadores': boxeadores}
    return render(request, 'Boxeo/boxeadores.html', data)



def agregarBoxeador(request):
    form = FormBoxeador()
    if request.method == 'POST':
        form = FormBoxeador(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'Boxeo/agregarBoxeador.html', data)

def eliminarBoxeador(request, id):
    boxeador = Boxeador.objects.get(id = id) 
    boxeador.delete()
    return redirect('/boxeadores')


def actualizarBoxeador(request, id):
    boxeador = Boxeador.objects.get(id = id)
    form = FormBoxeador(instance=boxeador)
    if request.method == 'POST' :
        form = FormBoxeador(request.POST, instance=boxeador)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form' : form}
    return render(request, 'Boxeo/agregarBoxeador.html', data)



    ###TORNEO###

def listadoTorneos(request):
    torneos = Torneo.objects.all()
    data = {'torneos': torneos}
    return render(request, 'Boxeo/torneos.html', data) 

def agregarTorneo(request):
    form = FormTorneo()
    if request.method == 'POST':
        form = FormTorneo(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'Boxeo/agregarTorneo.html', data)

def eliminarTorneo(request, id):
    torneo = Torneo.objects.get(id = id) 
    torneo.delete()
    return redirect('/torneos')

def actualizarTorneo(request, id):
    torneo = Torneo.objects.get(id = id)
    form = FormTorneo(instance=torneo)
    if request.method == 'POST' :
        form = FormTorneo(request.POST, instance=torneo)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form' : form}
    return render(request, 'Boxeo/agregarTorneo.html', data)



    ## TEAM ##

def listadoTeams(request):
    teams = Team.objects.all()
    data = {'teams': teams}
    return render(request, 'Boxeo/teams.html', data) 

def agregarTeam(request):
    form = FormTeam()
    if request.method == 'POST':
        form = FormTeam(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'Boxeo/agregarTeam.html', data)

def eliminarTeam(request, id):
    team = Team.objects.get(id = id) 
    team.delete()
    return redirect('/teams')

def actualizarTeam(request, id):
    team = Team.objects.get(id = id)
    form = FormTeam(instance=team)
    if request.method == 'POST' :
        form = FormTeam(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form' : form}
    return render(request, 'Boxeo/agregarTeam.html', data)


