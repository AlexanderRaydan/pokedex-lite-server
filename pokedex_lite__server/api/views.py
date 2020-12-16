from django.shortcuts import render
from rest_framework import viewsets
from core.serializer import PokemonSerializer

from api.models import Pokemon

# Create your views here.


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
