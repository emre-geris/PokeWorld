from django.urls import path
from . import views

app_name = "PokeApp"

urlpatterns = [
    path("",views.pokemon_list, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('favorite/<int:pokemon_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('api/pokemons/', views.api_pokemon_list, name="api_pokemon_list"),
    path('<slug:slug>/', views.pokemon_detail, name='pokemon_detail'),
]