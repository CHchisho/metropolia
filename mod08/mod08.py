import mysql.connector

# Tietokantayhteyden konfiguraatio
config = {
    'user': 'ilia',
    'password': 'password',
    'host': 'localhost',
    'database': 'flight_game',
    'port': 3306
}


def get_airport_by_icao(icao_code):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = "SELECT name, municipality FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))

        # Haetaan tulos
        result = cursor.fetchone()

        # Tarkistetaan löytyikö lentokenttää
        if result:
            airport_name, municipality = result
            print(f"Lentokenttä: {airport_name}, Sijaintikunta: {municipality}")
        else:
            print(f"ICAO-koodilla {icao_code} ei löydy lentokenttää.")

    except mysql.connector.Error as e:
        print(f"Virhe tietokantahaussa: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


icao_code = input("Anna lentoaseman ICAO-koodi: ").upper()
get_airport_by_icao(icao_code)


# 2
def get_airport_counts_by_type(country_code):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = """
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = %s 
        GROUP BY type
        """
        cursor.execute(query, (country_code,))

        results = cursor.fetchall()

        if results:
            print(f"Lentokenttien lukumäärät maassa {country_code}:")
            for airport_type, count in results:
                print(f"{airport_type}: {count} kappaletta")
        else:
            print(f"Maassa {country_code} ei löytynyt lentokenttiä.")

    except mysql.connector.Error as e:
        print(f"Virhe tietokantahaussa: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


country_code = input("Anna maakoodi (esimerkiksi FI): ").upper()  # Muutetaan syöte isoiksi kirjaimiksi
get_airport_counts_by_type(country_code)

# 3
from geopy.distance import geodesic
def get_airport_coordinates(icao_code):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))
        result = cursor.fetchone()

        if result:
            latitude, longitude = result
            return (latitude, longitude)
        else:
            print(f"ICAO-code {icao_code} not found.")
            return None

    except mysql.connector.Error as e:
        print(f"Virhe tietokantahaussa: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def calculate_distance_between_airports(icao1, icao2):
    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if coords1 and coords2:
        distance_km = geodesic(coords1, coords2).kilometers
        print(f"Etäisyys lentokenttien {icao1} ja {icao2} välillä: {distance_km:.2f} km")
    else:
        print("Lentokenttien välistä etäisyyttä ei voitu laskea.")


icao1 = input("Syötä ensimmäisen lentokentän ICAO-koodi:").upper()
icao2 = input("Syötä toisen lentokentän ICAO-koodi:").upper()
calculate_distance_between_airports(icao1, icao2)
