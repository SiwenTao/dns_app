# user_server.py
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fibonacci')
def get_fibonacci():
    hostname = request.args.get('hostname')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    # Resolve the FS IP address from the AS
    resolve_url = f"http://{as_ip}:{as_port}/resolve?hostname={hostname}"
    resolve_resp = requests.get(resolve_url)
    if resolve_resp.status_code != 200:
        return jsonify({"error": "Failed to resolve FS IP"}), resolve_resp.status_code

    fs_ip = resolve_resp.json()['ip']
    
    # Request Fibonacci number from FS
    fib_url = f"http://{fs_ip}:9090/fibonacci?number={number}"
    fib_resp = requests.get(fib_url)
    if fib_resp.status_code == 200:
        return fib_resp.json(), 200
    else:
        return jsonify({"error": "Failed to get Fibonacci number from FS"}), fib_resp.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
