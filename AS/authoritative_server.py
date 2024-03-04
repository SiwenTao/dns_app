# authoritative_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)
dns_records = {}

@app.route('/register', methods=['PUT'])
def register():
    data = request.json
    dns_records[data['hostname']] = data['ip']
    return jsonify({"message": "Registration successful"}), 201

@app.route('/resolve', methods=['GET'])
def resolve():
    hostname = request.args.get('hostname')
    ip_address = dns_records.get(hostname, "Not found")
    if ip_address == "Not found":
        return jsonify({"error": "Hostname not found"}), 404
    return jsonify({"ip": ip_address}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=53533)
