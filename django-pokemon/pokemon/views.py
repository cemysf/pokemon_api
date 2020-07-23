from django.shortcuts import render
from rest_framework import viewsets, filters
from . import models
from . import serializers

# Create your views here.
class PokemonView(viewsets.ReadOnlyModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer