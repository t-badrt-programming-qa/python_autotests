import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e5071329cbf9746280e9b2bf177596e0'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_changing = {
    "pokemon_id": "1323610", ##write id of pokemon that we need here.
    "name": "generate",
    "photo_id": -1
}
body_add_in_pokeball = {
    "pokemon_id": "1323721", ##write id of pokemon that we need here. 
}
## 1. First_backend_request_from_the_homework, create_pokemons.
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json())

## Saving_one_of_the_response_JSON_values (id).
pokemon_id = response_create.json()['id'] ## "id" is the key that we needed to search
print(pokemon_id)

## Saving_one_of_the_response_JSON_values_2 (message).
pokemon_id = response_create.json()['message'] ## "message" is the key that we needed to search
print(pokemon_id)'''

## 2. Second_backend_request_from_the_lecture, changing_pokemon_name.
'''response_changing = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changing)
print(response_changing.json())

## Saving_one_of_the_response_JSON_values (id).
pokemon_id = response_changing.json()['id'] ## "id" is the key that we needed to search
print(pokemon_id)

## Saving_one_of_the_response_JSON_values_2 (message).
pokemon_id = response_changing.json()['message'] ## "message" is the key that we needed to search
print(pokemon_id)'''

## 3. Third_backend_request_from_the_lecture, add_pokemon_in_pokeball.
'''response_add_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_in_pokeball)
print(response_add_in_pokeball.json())

## Saving_one_of_the_response_JSON_values (id).
pokemon_id = response_changing.json()['id'] ## "id" is the key that we needed to search
print(pokemon_id)

## Saving_one_of_the_response_JSON_values_2 (message).
pokemon_id = response_changing.json()['message'] ## "message" is the key that we needed to search
print(pokemon_id)'''