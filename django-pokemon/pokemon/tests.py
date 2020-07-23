from django.test import TestCase
from pokemon.models import Pokemon
from pokemon.handlers import *
from decimal import Decimal

# Create your tests here.
class PokemonHandlersTests(TestCase):
    def setUp(self):
        Pokemon.objects.create(
            name="legendary",
            type_1 = "n/a",
            type_2 = "n/a",
            total = 100,
            hp = 10,
            attack = 1,
            defense = 1.5,
            sp_atk = 3,
            sp_def = 0,
            speed = 4,
            generation = 1,
            legendary = True,
        )

        Pokemon.objects.create(
            name="ghost1",
            type_1 = "Ghost",
            type_2 = "n/a",
            total = 100,
            hp = 10,
            attack = 1,
            defense = 1.5,
            sp_atk = 3,
            sp_def = 0,
            speed = 4,
            generation = 1,
            legendary = False,
        )

        Pokemon.objects.create(
            name="ghost2",
            type_1 = "n/a",
            type_2 = "Ghost",
            total = 100,
            hp = 10,
            attack = 1,
            defense = 1.5,
            sp_atk = 3,
            sp_def = 0,
            speed = 4,
            generation = 1,
            legendary = True,
        )

        Pokemon.objects.create(
            name="steel",
            type_1 = "Steel",
            type_2 = "n/a",
            total = 100,
            hp = 10,
            attack = 1,
            defense = 1.5,
            sp_atk = 3,
            sp_def = 0,
            speed = 4,
            generation = 1,
            legendary = False,
        )

        Pokemon.objects.create(
            name="fire",
            type_1 = "Fire",
            type_2 = "n/a",
            total = 100,
            hp = 10,
            attack = 1,
            defense = 1.5,
            sp_atk = 3,
            sp_def = 0,
            speed = 4,
            generation = 1,
            legendary = False,
        )

        Pokemon.objects.create(
            name="bug_fly",
            type_1 = "Bug",
            type_2 = "Flying",
            total = 100,
            hp = 10,
            attack = 1,
            defense = 1.5,
            sp_atk = 3,
            sp_def = 0,
            speed = 4,
            generation = 1,
            legendary = False,
        )

        Pokemon.objects.create(
            name="Gaaaa",
            type_1 = "n/a",
            type_2 = "n/a",
            total = 100,
            hp = 10,
            attack = 1,
            defense = 1.5,
            sp_atk = 3,
            sp_def = 0,
            speed = 4,
            generation = 1,
            legendary = False,
        )


    def test_exclude_legendary(self):
        obj = Pokemon.objects.get(name="legendary")
        with self.assertRaises(ValueError):
            handle_legendary(obj)

    def test_exclude_ghost(self):
        obj = Pokemon.objects.get(name="ghost1")
        with self.assertRaises(ValueError):
            handle_ghost(obj)

    def test_exclude_legendary_and_ghost(self):
        obj = Pokemon.objects.get(name="ghost2")
        with self.assertRaises(ValueError):
            handle_legendary(obj)
        with self.assertRaises(ValueError):
            handle_ghost(obj)

    def test_steel(self):
        obj = Pokemon.objects.get(name="steel")
        hp_prev = obj.hp
        handle_steel(obj)
        hp_new = obj.hp
        self.assertEqual(hp_prev * 2, hp_new)

    def test_fire(self):
        obj = Pokemon.objects.get(name="fire")
        atk_prev = obj.attack
        handle_fire(obj)
        atk_new = obj.attack
        self.assertEqual(atk_prev * Decimal(0.9), atk_new)

    def test_bug_and_flying(self):
        obj = Pokemon.objects.get(name="bug_fly")
        spd_prev = obj.speed
        handle_bugAndFlying(obj)
        spd_new = obj.speed
        self.assertEqual(spd_prev * Decimal(1.1), spd_new)

    def test_starts_with_letter_g(self):
        obj = Pokemon.objects.get(name="Gaaaa")
        def_prev = obj.defense
        handle_nameStartWithG(obj)
        def_new = obj.defense
        self.assertEqual(def_prev + 20, def_new)
