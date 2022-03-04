import requests
def run():


    url = "https://pokeapi.co/api/v2/type/fighting"
    peso_max = 0
    peso_min = 1000000
    response = requests.get(url)
    if response.status_code == 200:

        pokemon_json = response.json()
        pokemones_fighting = pokemon_json.get("pokemon", [])

        if pokemones_fighting:
            for pokemon in pokemones_fighting:
                url = (pokemon["pokemon"]["url"])
                response = requests.get(url)
                if response.status_code == 200:
                    info_pokemon = response.json()
                    pokemones_id = info_pokemon["id"]
                    if pokemones_id <= 151:
                        pokemon_weight = info_pokemon["weight"]
                        peso_max = max(pokemon_weight, peso_max)
                        peso_min = min(pokemon_weight, peso_min)

    print("[ " + str(peso_max) + " , " + str(peso_min) + "]")

if __name__ == "__main__":
    run()              