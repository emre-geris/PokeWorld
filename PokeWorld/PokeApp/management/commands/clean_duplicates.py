from django.core.management.base import BaseCommand
from PokeApp.models import Pokemon, Favorite
from django.db.models import Count

class Command(BaseCommand):
    help = "Clean up duplicate Pokémon entries in the database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting duplicate cleanup...")
        
        # Find duplicates by name
        duplicates = Pokemon.objects.values('name').annotate(
            count=Count('id')
        ).filter(count__gt=1)
        
        if not duplicates:
            self.stdout.write(self.style.SUCCESS("No duplicates found!"))
            return
        
        self.stdout.write(f"Found {len(duplicates)} Pokémon with duplicates:")
        
        for duplicate in duplicates:
            pokemon_name = duplicate['name']
            pokemon_count = duplicate['count']
            
            self.stdout.write(f"  - {pokemon_name}: {pokemon_count} entries")
            
            # Get all instances of this Pokémon
            pokemon_instances = Pokemon.objects.filter(name=pokemon_name).order_by('id')
            
            # Keep the first one, delete the rest
            first_pokemon = pokemon_instances.first()
            duplicates_to_delete = pokemon_instances.exclude(id=first_pokemon.id)
            
            # Get IDs of duplicates to delete
            duplicate_ids = list(duplicates_to_delete.values_list('id', flat=True))
            
            # Update favorites to point to the first Pokémon
            Favorite.objects.filter(pokemon_id__in=duplicate_ids).update(
                pokemon=first_pokemon
            )
            
            # Delete duplicate Pokémon
            deleted_count = duplicates_to_delete.delete()[0]
            
            self.stdout.write(f"    → Kept ID {first_pokemon.id}, deleted {deleted_count} duplicates")
        
        # Check for duplicates by slug as well
        slug_duplicates = Pokemon.objects.values('slug').annotate(
            count=Count('id')
        ).filter(count__gt=1)
        
        if slug_duplicates:
            self.stdout.write(f"\nFound {len(slug_duplicates)} Pokémon with duplicate slugs:")
            
            for duplicate in slug_duplicates:
                pokemon_slug = duplicate['slug']
                pokemon_count = duplicate['count']
                
                self.stdout.write(f"  - {pokemon_slug}: {pokemon_count} entries")
                
                # Get all instances of this Pokémon by slug
                pokemon_instances = Pokemon.objects.filter(slug=pokemon_slug).order_by('id')
                
                # Keep the first one, delete the rest
                first_pokemon = pokemon_instances.first()
                duplicates_to_delete = pokemon_instances.exclude(id=first_pokemon.id)
                
                # Get IDs of duplicates to delete
                duplicate_ids = list(duplicates_to_delete.values_list('id', flat=True))
                
                # Update favorites to point to the first Pokémon
                Favorite.objects.filter(pokemon_id__in=duplicate_ids).update(
                    pokemon=first_pokemon
                )
                
                # Delete duplicate Pokémon
                deleted_count = duplicates_to_delete.delete()[0]
                
                self.stdout.write(f"    → Kept ID {first_pokemon.id}, deleted {deleted_count} duplicates")
        
        # Final count
        total_pokemon = Pokemon.objects.count()
        self.stdout.write(self.style.SUCCESS(f"\nCleanup complete! Total Pokémon: {total_pokemon}"))
        
        # Verify no duplicates remain
        name_duplicates = Pokemon.objects.values('name').annotate(
            count=Count('id')
        ).filter(count__gt=1)
        
        slug_duplicates = Pokemon.objects.values('slug').annotate(
            count=Count('id')
        ).filter(count__gt=1)
        
        if not name_duplicates and not slug_duplicates:
            self.stdout.write(self.style.SUCCESS("✓ No duplicates remain in the database"))
        else:
            self.stdout.write(self.style.WARNING("⚠ Some duplicates may still exist"))
