from . import models
from rest_framework import serializers


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = "__all__"