from .models import PERRO
from rest_framework import viewsets
from blog.serializers import PERROSerializer


class PERROViewSet(viewsets.ModelViewSet):
    queryset = PERRO.objects.all()
    serializer_class = PERROSerializer