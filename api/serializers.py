from rest_framework import serializers
from Boxeo.models import Boxeador,Torneo,Team

class BoxeadorSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Boxeador
        fields = '__all__'

class TorneoSerialier(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'