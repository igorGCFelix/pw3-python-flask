from flask import render_template, request, url_for, redirect
import urllib.request
import json

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/pokemon')
    def pokemon():
        # Buscando lista de pokémons da API
        url = 'https://pokeapi.co/api/v2/pokemon?limit=20'
        response = urllib.request.urlopen(url)
        apiData = response.read()
        pokemonList = json.loads(apiData)
        
        # Buscando dados detalhados de cada pokémon
        pokemons = []
        for pokemon in pokemonList['results']:
            pokemon_url = pokemon['url']
            pokemon_response = urllib.request.urlopen(pokemon_url)
            pokemon_data = json.loads(pokemon_response.read())
            
            pokemon_info = {
                'id': pokemon_data['id'],
                'name': pokemon_data['name'].title(),
                'image': pokemon_data['sprites']['front_default'],
                'types': [type_info['type']['name'].title() for type_info in pokemon_data['types']]
            }
            pokemons.append(pokemon_info)
        
        return render_template('pokemon.html', pokemons=pokemons)
    
    @app.route('/pokemon/<int:id>')
    def pokemon_detail(id):
        # Buscando dados detalhados do pokémon específico
        url = f'https://pokeapi.co/api/v2/pokemon/{id}'
        try:
            response = urllib.request.urlopen(url)
            apiData = response.read()
            pokemon_data = json.loads(apiData)
            
            pokemon_info = {
                'id': pokemon_data['id'],
                'name': pokemon_data['name'].title(),
                'image': pokemon_data['sprites']['front_default'],
                'types': [type_info['type']['name'].title() for type_info in pokemon_data['types']],
                'height': pokemon_data['height'],  
                'weight': pokemon_data['weight'], 
                'abilities': [ability['ability']['name'].title() for ability in pokemon_data['abilities']],
                'stats': [
                    {
                        'name': stat['stat']['name'].title(),
                        'value': stat['base_stat']
                    } for stat in pokemon_data['stats']
                ]
            }
            
            return render_template('pokemoninfo.html', pokemon=pokemon_info)
        except:
            return render_template('error.html', message=f'Pokémon com ID {id} não foi encontrado.')

