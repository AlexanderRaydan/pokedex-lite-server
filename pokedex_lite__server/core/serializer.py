
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id','Uid' ,'name' , 'type' , 'level' , 'evolution_level' , 'image' , 'evolution_to' , 'abilities' ]