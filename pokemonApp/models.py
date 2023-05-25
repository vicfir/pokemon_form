from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Pokemon(models.Model):
    class Type(models.TextChoices):
        PLANTE = 'Plante'
        FEU = 'Feu'
        EAU = 'Eau'
        INSECTE = 'Insecte'
        NORMAL = 'Normal'
        COMBAT = 'Combat'
    nom = models.fields.CharField(max_length=30)
    type = models.fields.CharField(choices=Type.choices,max_length=10)
    niveau = models.fields.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    class Meta:
        db_table="pokemons"