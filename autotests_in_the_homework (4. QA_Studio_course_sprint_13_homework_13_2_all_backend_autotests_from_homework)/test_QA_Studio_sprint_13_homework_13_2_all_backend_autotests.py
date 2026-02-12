## 'test' in the name of file is just for the testing in the "testing" tab.

import requests 
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'your_token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 'your_trainer_id'
## 1. First_backend_autotest_from_the_lecture, check_status_code_in_response.
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : TRAINER_ID})
    assert response.status_code == 200
## 2. Second_backend_autotest, check_one_of_the_values_in_JSON_in_response_(name).
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {"trainer_id" : TRAINER_ID})
    print(response_get.json())
    assert response_get.json()["data"][0]["name"] == 'scyther'
## 3. Parametrized_backend_autotests.
## Step 1,fixture.
@pytest.mark.parametrize("key, value", [('name', 'scyther'), ('trainer_id', TRAINER_ID), ('pokemon_id', '1323721')])
## Step 2. Defining function for parameters from step 1.
def test_parametrize(key,value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {"trainer_id" : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
## 4. Experiments with Pytest code.
import pytest
import requests
import json # Импортируем модуль json для красивого вывода

## ... (URL и TRAINER_ID должны быть определены) ...

@pytest.mark.parametrize("key, value", [
    ('name', 'scyther'), 
    ('trainer_id', TRAINER_ID), 
    ('id', '1323721')
])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/pokemons', params={"trainer_id" : TRAINER_ID})
    
    # --- ДОБАВЬТЕ ЭТИ СТРОКИ ДЛЯ ОТЛАДКИ ---
    try:
        data = response_parametrize.json()["data"]
        print(f"\n--- Структура данных в ответе для первого покемона ---")
        # Используем json.dumps для форматированного вывода словаря
        print(json.dumps(data, indent=4, ensure_ascii=False)) 
        print(f"--- Конец структуры данных ---")
    except Exception as e:
        print(f"\nНе удалось распарсить JSON или получить доступ к ключу 'data': {e}")
    # ----------------------------------------
    
    # Эта строка вызывает ошибку, когда key == 'pokemon_id'
    assert response_parametrize.json()["data"][0][key] == value