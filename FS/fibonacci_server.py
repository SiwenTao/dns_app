
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def register_with_as():
    as_url = "http://as:53533/register"
    registration_details = {
        "hostname": "fibonacci.com",
        "ip": "fs"
    }
    response = requests.put(as_url, json=registration_details)
    print("Registration response:", response.text)

@app.route('/fibonacci')
def fibonacci():
    number = request.args.get('number', default=1, type=int)
    a, b = 0, 1
    for _ in range(number):
        a, b = b, a + b
    return jsonify({"Fibonacci": a})

if __name__ == '__main__':
    register_with_as()
    app.run(host='0.0.0.0', port=9090)
