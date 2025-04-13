from rest_framework import serializers
from .models import *

class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    ism = serializers.CharField(min_length=3)
    davlat = serializers.CharField()
    jins = serializers.CharField()
    t_sana = serializers.DateField()

class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    nom = serializers.CharField(min_length=3)
    narx = serializers.FloatField()
    izoh = serializers.CharField()
    davomiylik = serializers.DurationField()

class KinoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Kino
        fields = '__all__'

class KinoPostSerializer(serializers.ModelSerializer):
    class Meta:
        models = Kino
        fields = '__all__'