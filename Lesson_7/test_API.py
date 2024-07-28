import requests

Base_URL = "https://api.kinopoisk.dev/v1.4"

def test_search():
    my_headers = {"X-API-KEY": 'H09YKK0-G2NMX2A-JFKDJQH-W86Q6HH'}
    result = requests.get(Base_URL + '/movie?page=1&limit=1&id=5304403', headers = my_headers)
    assert result.status_code == 200


    
