import requests
def run():


    url = "https://pokeapi.co/api/v2/pokemon/?limit=1126"
    count_pokemon = 0
    response = requests.get(url)
    if response.status_code == 200:

        pokemon_json = response.json()
        pokemones = pokemon_json.get("results", [])

        if pokemones:
            for pokemon in pokemones:
                name = pokemon["name"]
                if "at" in name and name.count("a") == 2:
                        count_pokemon = count_pokemon + 1                    
    print(count_pokemon)

if __name__ == "__main__":
    run()                      