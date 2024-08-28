from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Т конфигурация для подключения к базе данных
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
        result = cursor.fetchone()

        if result:
            airport_name, municipality = result
            return {
                "ICAO": icao_code,
                "Name": airport_name,
                "Municipality": municipality
            }
        else:
            return None

    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


@app.route('/kentta/<icao_code>', methods=['GET'])
def kentta(icao_code):
    icao_code = icao_code.upper()
    airport_info = get_airport_by_icao(icao_code)

    if airport_info:
        return jsonify(airport_info)
    else:
        return jsonify({"error": "ICAO code not found"}), 404


if __name__ == '__main__':
    app.run(host='localhost', port=7737)
