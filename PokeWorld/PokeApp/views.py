# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Min

# Local imports
from . import models
from .models import Favorite

# Third-party imports
import pandas as pd
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Color constants
TYPE_COLORS = {
    "Grass": "text-green-600",
    "Poison": "text-purple-600",
    "Fire": "text-red-500",
    "Water": "text-blue-500",
    "Electric": "text-yellow-400",
    "Ice": "text-cyan-400",
    "Fighting": "text-orange-600",
    "Ground": "text-yellow-700",
    "Flying": "text-indigo-400",
    "Psychic": "text-pink-500",
    "Bug": "text-lime-500",
    "Rock": "text-gray-500",
    "Ghost": "text-purple-800",
    "Dragon": "text-indigo-800",
    "Dark": "text-gray-800",
    "Steel": "text-gray-400",
    "Fairy": "text-pink-300",
    "Normal": "text-gray-700"
}

TYPE_BG_COLORS = {
    "Grass": "bg-green-500",
    "Poison": "bg-purple-500",
    "Fire": "bg-red-500",
    "Water": "bg-blue-500",
    "Electric": "bg-yellow-400",
    "Ice": "bg-cyan-400",
    "Fighting": "bg-orange-500",
    "Ground": "bg-yellow-600",
    "Flying": "bg-indigo-400",
    "Psychic": "bg-pink-500",
    "Bug": "bg-lime-500",
    "Rock": "bg-gray-500",
    "Ghost": "bg-purple-600",
    "Dragon": "bg-indigo-600",
    "Dark": "bg-gray-700",
    "Steel": "bg-gray-400",
    "Fairy": "bg-pink-300",
    "Normal": "bg-gray-500"
}

CHART_COLORS = {
    "Grass": "#10b981",      # green-500
    "Poison": "#8b5cf6",     # purple-500
    "Fire": "#ef4444",       # red-500
    "Water": "#3b82f6",      # blue-500
    "Electric": "#facc15",   # yellow-400
    "Ice": "#22d3ee",        # cyan-400
    "Fighting": "#f97316",   # orange-500
    "Ground": "#ca8a04",     # yellow-600
    "Flying": "#818cf8",     # indigo-400
    "Psychic": "#ec4899",    # pink-500
    "Bug": "#84cc16",        # lime-500
    "Rock": "#6b7280",       # gray-500
    "Ghost": "#9333ea",      # purple-600
    "Dragon": "#6366f1",     # indigo-600
    "Dark": "#374151",       # gray-700
    "Steel": "#9ca3af",      # gray-400
    "Fairy": "#f9a8d4",      # pink-300
    "Normal": "#6b7280"      # gray-500
}

# User Registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('PokeApp:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('PokeApp:home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# User Logout
def logout_view(request):
    logout(request)
    return redirect('PokeApp:home')

# Favorite/Unfavorite API
@login_required
def toggle_favorite(request, pokemon_id):
    if request.method == 'POST':
        pokemon = get_object_or_404(models.Pokemon, id=pokemon_id)
        fav, created = Favorite.objects.get_or_create(user=request.user, pokemon=pokemon)
        if not created:
            fav.delete()
            return JsonResponse({'status': 'removed'})
        return JsonResponse({'status': 'added'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def pokemon_list(request):
    # Get unique Pokémon by name to avoid duplicates
    pokemon_ids = models.Pokemon.objects.values('name').annotate(
        id=Min('id')
    ).values_list('id', flat=True)
    
    # Get the actual Pokémon objects
    pokemons = models.Pokemon.objects.filter(id__in=pokemon_ids).order_by('id')
    
    user_favs = []
    if request.user.is_authenticated:
        user_favs = Favorite.objects.filter(user=request.user).values_list('pokemon_id', flat=True)
    
    for p in pokemons:
        t1 = (p.type1 or "").capitalize()
        t2 = (p.type2 or "").capitalize() if p.type2 else None
        p.color1 = TYPE_COLORS.get(t1, "text-gray-600")
        p.color2 = TYPE_COLORS.get(t2, "text-gray-600") if t2 else None
        p.is_favorite = p.id in user_favs
    
    return render(request, "base.html", {"pokemons": pokemons})

def api_pokemon_list(request):
    page = int(request.GET.get('page', 1))
    page_size = 20
    # Get unique Pokémon by name to avoid duplicates
    pokemon_ids = models.Pokemon.objects.values('name').annotate(
        id=Min('id')
    ).values_list('id', flat=True)
    
    # Get the actual Pokémon objects
    pokemons = models.Pokemon.objects.filter(id__in=pokemon_ids).order_by('id')
    paginator = Paginator(pokemons, page_size)
    page_obj = paginator.get_page(page)
    results = []
    for p in page_obj:
        t1 = (p.type1 or "").capitalize()
        t2 = (p.type2 or "").capitalize() if p.type2 else None
        color1 = TYPE_COLORS.get(t1, "text-gray-600")
        color2 = TYPE_COLORS.get(t2, "text-gray-600") if t2 else None
        results.append({
            'name': p.name,
            'slug': p.slug,
            'image_url': p.image_url,
            'type1': t1,
            'type2': t2,
            'color1': color1,
            'color2': color2,
            'hp': p.hp,
            'attack': p.attack,
            'defense': p.defense,
            'detail_url': reverse('PokeApp:pokemon_detail', args=[p.slug]),
        })
    return JsonResponse({'results': results})

@login_required
def favorites_view(request):
    user_favs = Favorite.objects.filter(user=request.user).select_related('pokemon')
    pokemons = [fav.pokemon for fav in user_favs]
    
    for p in pokemons:
        t1 = (p.type1 or "").capitalize()
        t2 = (p.type2 or "").capitalize() if p.type2 else None
        p.color1 = "text-gray-600"  # Default text color
        p.color2 = "text-gray-600" if t2 else None
        p.bg_color1 = TYPE_BG_COLORS.get(t1, "bg-gray-500")
        p.bg_color2 = TYPE_BG_COLORS.get(t2, "bg-gray-500") if t2 else None
    
    return render(request, 'PokeApp/favorites.html', {'pokemons': pokemons})

def pokemon_detail(request, slug):
    pokemon = get_object_or_404(models.Pokemon, slug=slug)

    # Set text colors for other templates
    pokemon.color1 = TYPE_COLORS.get(pokemon.type1.capitalize(), "text-gray-600")
    pokemon.color2 = TYPE_COLORS.get(pokemon.type2.capitalize(), "text-gray-600") if pokemon.type2 else None
    
    # Set background colors for type badges in detail template
    pokemon.bg_color1 = TYPE_BG_COLORS.get(pokemon.type1.capitalize(), "bg-gray-500")
    pokemon.bg_color2 = TYPE_BG_COLORS.get(pokemon.type2.capitalize(), "bg-gray-500") if pokemon.type2 else None

    # Get chart colors based on primary type
    primary_type = pokemon.type1.capitalize()
    chart_color = CHART_COLORS.get(primary_type, "#6b7280")  # Default to gray if type not found
    
    # Get secondary type color if Pokémon has dual types
    secondary_chart_color = None
    if pokemon.type2:
        secondary_type = pokemon.type2.capitalize()
        secondary_chart_color = CHART_COLORS.get(secondary_type, "#6b7280")

    # Prepare stats data
    stats = {
        'stat': ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'],
        'value': [pokemon.hp, pokemon.attack, pokemon.defense, pokemon.sp_attack, pokemon.sp_defense, pokemon.speed]
    }
    df = pd.DataFrame(stats)

    # Generate Radar Chart with type color
    categories = df['stat'].tolist()
    values = df['value'].tolist()
    values += values[:1]

    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
    
    # Use gradient effect for dual-type Pokémon
    if secondary_chart_color:
        ax.plot(angles, values, color=chart_color, linewidth=2)
        ax.fill(angles, values, color=chart_color, alpha=0.3)
        # Add a subtle overlay with secondary color
        ax.fill(angles, values, color=secondary_chart_color, alpha=0.1)
    else:
        ax.plot(angles, values, color=chart_color, linewidth=2)
        ax.fill(angles, values, color=chart_color, alpha=0.25)
    
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)

    radar_path = os.path.join(settings.MEDIA_ROOT, 'pokemon_charts', f'radar_{pokemon.slug}.png')
    os.makedirs(os.path.dirname(radar_path), exist_ok=True)
    plt.savefig(radar_path, bbox_inches='tight')
    plt.close()

    # Generate Bar Chart with type color
    plt.figure(figsize=(6,4))
    
    if secondary_chart_color:
        # Create alternating colors for dual-type Pokémon
        custom_palette = []
        for i in range(len(df)):
            if i % 2 == 0:
                custom_palette.append(chart_color)
            else:
                custom_palette.append(secondary_chart_color)
    else:
        # Use single color for single-type Pokémon
        custom_palette = [chart_color] * len(df)
    
    sns.barplot(x='stat', y='value', data=df, palette=custom_palette)
    plt.title(f"{pokemon.name} Stats")
    bar_path = os.path.join(settings.MEDIA_ROOT, 'pokemon_charts', f'bar_{pokemon.slug}.png')
    plt.savefig(bar_path, bbox_inches='tight')
    plt.close()

    # Prepare context for template
    context = {
        'pokemon': pokemon,
        'radar_chart_url': f'{settings.MEDIA_URL}pokemon_charts/radar_{pokemon.slug}.png',
        'bar_chart_url': f'{settings.MEDIA_URL}pokemon_charts/bar_{pokemon.slug}.png',
        'color1': pokemon.color1,
        'color2': pokemon.color2
    }

    return render(request, 'PokeApp/pokemon_detail.html', context)