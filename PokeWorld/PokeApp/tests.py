from django.test import TestCase
from django.contrib.auth.models import User
from .models import Pokemon, Favorite

# Create your tests here.
class PokemonModelTest(TestCase):
    def setUp(self):
        self.pokemon = Pokemon.objects.create(
            name="TestPokemon",
            type1="Fire",
            type2="Flying",
            hp=100,
            attack=80,
            defense=70,
            sp_attack=90,
            sp_defense=75,
            speed=85,
            image_url="https://example.com/test.png"
        )
    
    def test_pokemon_creation(self):
        self.assertEqual(self.pokemon.name, "TestPokemon")
        self.assertEqual(self.pokemon.type1, "Fire")
        self.assertEqual(self.pokemon.slug, "testpokemon")
    
    def test_pokemon_str_method(self):
        self.assertEqual(str(self.pokemon), "TestPokemon")

class FavoriteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.pokemon = Pokemon.objects.create(
            name="TestPokemon",
            type1="Fire",
            hp=100,
            attack=80,
            defense=70,
            sp_attack=90,
            sp_defense=75,
            speed=85
        )
        self.favorite = Favorite.objects.create(
            user=self.user,
            pokemon=self.pokemon
        )
    
    def test_favorite_creation(self):
        self.assertEqual(self.favorite.user, self.user)
        self.assertEqual(self.favorite.pokemon, self.pokemon)
    
    def test_favorite_str_method(self):
        expected = f"{self.user.username} - {self.pokemon.name}"
        self.assertEqual(str(self.favorite), expected)
