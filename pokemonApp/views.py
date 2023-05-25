from django.shortcuts import render,redirect
from .models import Pokemon
from .forms import PokemonForm

# Create your views here.
def home(request):
  pokemons = Pokemon.objects.all()

  return render(request, 'home.html', { 'pokemons' : pokemons })

def pokemon_create(request):
  if request.method == 'POST' :
    form = PokemonForm(request.POST)
    if form.is_valid():
      pokemon = form.save()
      return redirect('home')
  else :
    form = PokemonForm()
  
  return render(request, 'pokemon_form.html', {'form':form})