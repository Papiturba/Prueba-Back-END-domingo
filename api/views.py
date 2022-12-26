from django.shortcuts import render
from .serializers import BoxeadorSeriaLizer,TorneoSerialier,TeamSerializer
from Boxeo.models import Boxeador,Torneo,Team
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics, mixins

# Create your views here.
class Boxeador_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Boxeador.objects.all()
    serializer_class = BoxeadorSeriaLizer
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)



class Boxeador_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Boxeador.objects.all()
    serializer_class = BoxeadorSeriaLizer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class Torneo_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerialier
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Torneo_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerialier

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class Team_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Team_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
