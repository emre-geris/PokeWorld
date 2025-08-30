from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, null=True, blank=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    image_url = models.URLField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)  
    # Images saved as url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # örn: "Pikachu" -> "pikachu"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'pokemon')
    def __str__(self):
        return f"{self.user.username} - {self.pokemon.name}"
