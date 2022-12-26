from django.db import models


# Clase Boxeador

class Boxeador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    peso = models.FloatField()
    cinturones = models.IntegerField()
    ko = models.IntegerField()

    def mostrar_boxeador(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.mostrar_boxeador()
    

  



#Clase Team
class Team(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    titulos = models.IntegerField()
    entrenador = models.CharField(max_length=60)
    lesionados = models.CharField(max_length=15)
    boxeador = models.ForeignKey(Boxeador,null=True,blank=True, on_delete=models.CASCADE)  

    def mostrar_team(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.mostrar_team()

    

    

    
    


##Clase Torneo


class Torneo(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    cupos = models.IntegerField()
    categoria = models.CharField(max_length=20)
    fecha = models.DateField()
    inscripcion = models.CharField(max_length=20)
    inscritos = models.ForeignKey(Team,null=True,blank=True, on_delete=models.CASCADE) 

    def mostrar_torneo(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.mostrar_torneo()