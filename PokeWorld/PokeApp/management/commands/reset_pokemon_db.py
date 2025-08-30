from django.core.management.base import BaseCommand
from PokeApp.models import Pokemon, Favorite

class Command(BaseCommand):
    help = "Reset Pokémon database and fetch fresh data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting database reset...")
        
        # Delete all favorites first (to avoid foreign key constraints)
        favorites_count = Favorite.objects.count()
        Favorite.objects.all().delete()
        self.stdout.write(f"Deleted {favorites_count} favorites")
        
        # Delete all Pokémon
        pokemon_count = Pokemon.objects.count()
        Pokemon.objects.all().delete()
        self.stdout.write(f"Deleted {pokemon_count} Pokémon")
        
        self.stdout.write(self.style.SUCCESS("Database reset complete!"))
        self.stdout.write("Now run: python manage.py fetch_pokemon")
