from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class PokemonView(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer