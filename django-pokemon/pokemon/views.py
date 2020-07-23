from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from . import models
from . import serializers
#from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PokemonView(viewsets.ReadOnlyModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Pokemon.objects.all()

    serializer_class = serializers.PokemonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
