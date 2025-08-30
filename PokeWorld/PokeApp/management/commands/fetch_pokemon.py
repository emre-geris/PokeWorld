from django.core.management.base import BaseCommand
from django.utils.text import slugify
import requests
from tqdm import tqdm
from PokeApp.models import Pokemon

class Command(BaseCommand):
    help = "Fetch Pokémon data from PokeAPI and save to DB"

    def handle(self, *args, **kwargs):
        n = 50  # Amount of pokemon that fetched
        for i in tqdm(range(1, n+1)):
            url = f"https://pokeapi.co/api/v2/pokemon/{i}"
            response = requests.get(url)
            data = response.json()
            
            stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
            types = [t['type']['name'] for t in data['types']]
            
            pokemon_name = data['name'].capitalize()
            pokemon_slug = slugify(pokemon_name)
            
            Pokemon.objects.update_or_create(
                slug=pokemon_slug,
                defaults={
                    'name': pokemon_name,
                    'type1': types[0],
                    'type2': types[1] if len(types) > 1 else None,
                    'hp': stats['hp'],
                    'attack': stats['attack'],
                    'defense': stats['defense'],
                    'sp_attack': stats['special-attack'],
                    'sp_defense': stats['special-defense'],
                    'speed': stats['speed'],
                    'image_url': data['sprites']['other']['official-artwork']['front_default']
                }
            )
        self.stdout.write(self.style.SUCCESS(f"{n} Pokémon data fetched and saved!"))
