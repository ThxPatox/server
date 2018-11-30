from .models import PERRO
from rest_framework import serializers

class PERROSerializer(serializers.HyperlinkedModelSerializer):
    adoptador = serializers.CharField(source='adoptador.username')
    class Meta:
        model = PERRO
        fields=('adoptador','nombreperro','raza','descripcion','estado','foto')