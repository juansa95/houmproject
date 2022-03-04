import requests
def run():


    url = "https://pokeapi.co/api/v2/egg-group/6"
    count_pokemon = 0
    response = requests.get(url)
    if response.status_code == 200:

        pokemon_json = response.json()
        pokemones_species = pokemon_json.get("pokemon_species", [])

        if pokemones_species:
            for pokemon in pokemones_species:
                name = pokemon["name"]
                if name != "raichu":
                        count_pokemon = count_pokemon + 1                    
    print(count_pokemon)

if __name__ == "__main__":
    run()              