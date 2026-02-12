import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'your_token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "your_email",
    "password": "your_password",
    "password_re": "repeat_your_password_here"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "generate",
    "photo_id": -1
}
## 1. First_backend_request_from_the_lecture, trainer_registration.
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''
## 2. Second_backend_request_from_the_lecture, trainer_email_confirmation.
'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''
## 3. Third_backend_request_from_the_lecture, create_pokemons.
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
print(response_create.status_code)

## Saving_one_of_the_response_JSON_values (id).
pokemon_id = response_create.json()['id'] ## "id" is the key that we needed to search
print(pokemon_id)

## Saving_one_of_the_response_JSON_values_2 (message).
pokemon_id = response_create.json()['message'] ## "id" is the key that we needed to search
print(pokemon_id)'''
