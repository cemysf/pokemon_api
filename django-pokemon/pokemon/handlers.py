from .models import Pokemon
from decimal import Decimal

def handle_legendary(pokemon: Pokemon):
    if pokemon.legendary == "True" or pokemon.legendary == True:
        raise ValueError("Invalid pokemon type")

def handle_ghost(pokemon: Pokemon):
    if pokemon.has_type("Ghost"):
        raise ValueError("Invalid pokemon type")

def handle_steel(pokemon: Pokemon):
    if pokemon.has_type("Steel"):
        pokemon.hp = Decimal(pokemon.hp) * Decimal(2)

def handle_fire(pokemon: Pokemon):
    if pokemon.has_type("Fire"):
        pokemon.attack = Decimal(pokemon.attack) * Decimal(0.9)

def handle_bugAndFlying(pokemon: Pokemon):
    if pokemon.has_type("Bug") and pokemon.has_type("Flying"):
        pokemon.speed = Decimal(pokemon.speed) * Decimal(1.1)

def handle_nameStartWithG(pokemon: Pokemon):
    if pokemon.name[0] == "G":
        len_name = len(pokemon.name)-1
        pokemon.defense = Decimal(pokemon.defense) + Decimal(len_name*5)