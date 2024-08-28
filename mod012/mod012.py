# 1
import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            vitsi = data['value']

            print(vitsi)
        else:
            print("Ei voitu hakea vitsiä, yritä uudelleen myöhemmin.")

    except requests.exceptions.RequestException as e:
        print(f"Virhe: {e}")


hae_chuck_norris_vitsi()

# 2
import requests

def hae_saa(paikkakunta, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            description = data['weather'][0]['description']
            lampotila_k = data['main']['temp']

            lampotila_c = lampotila_k - 273.15

            print(f"Sää paikkakunnalla {paikkakunta.capitalize()}: {description}")
            print(f"Lämpötila: {lampotila_c:.2f} °C")
        else:
            print(response.status_code)
            print(f"Ei löytynyt säädataa paikkakunnalle {paikkakunta}. Tarkista paikkakunnan nimi.")

    except requests.exceptions.RequestException as e:
        print(f"Virhe: {e}")


paikkakunta = input("Anna paikkakunnan nimi: ")
api_key = "2184240e955cb6a596c0207912cf6057"

hae_saa(paikkakunta, api_key)
