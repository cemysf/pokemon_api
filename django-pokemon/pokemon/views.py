from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from rest_framework.filters import SearchFilter
from . import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class PokemonView(viewsets.ReadOnlyModelViewSet):
    search_fields = ['name']
    filter_backends = (SearchFilter, DjangoFilterBackend)
    queryset = models.Pokemon.objects.all()

    serializer_class = serializers.PokemonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_fields = {
        'hp': ['gte', 'lte', 'exact'],
        'attack': ['gte', 'lte', 'exact'],
        'defense': ['gte', 'lte', 'exact'],
    }