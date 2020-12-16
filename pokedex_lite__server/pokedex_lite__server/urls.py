from django.contrib import admin
from django.urls import path

from rest_framework import routers

from api.views import PokemonViewSet
from django.conf.urls import include

route = routers.DefaultRouter()
route.register('pokemons' , PokemonViewSet )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , include(route.urls)),
]
