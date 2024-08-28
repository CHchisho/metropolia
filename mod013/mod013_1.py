# 1

from flask import Flask, jsonify
app = Flask(__name__)

def onko_alkuluku(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/alkuluku/<int:number>', methods=['GET'])
def alkuluku(number):
    is_prime = onko_alkuluku(number)
    response = {
        "Number": number,
        "isPrime": is_prime
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='localhost', port=7737)
