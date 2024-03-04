import socket
import json

# Configuration for the AS
AS_IP = '127.0.0.1'  # Use the correct IP address for your AS
AS_PORT = 53533  # Port on which your AS is listening

def send_udp_message(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Convert the message dictionary to a JSON string
        message_json = json.dumps(message)
        # Send the JSON message
        sock.sendto(message_json.encode(), (AS_IP, AS_PORT))
        # Receive the response
        response, _ = sock.recvfrom(4096)
        print("Received response:", response.decode())
    finally:
        sock.close()

# Example registration message
registration_message = {
    "TYPE": "A",
    "NAME": "fibonacci.com",
    "VALUE": "172.18.0.2",
    "TTL": "10"
}

# Example DNS query message
query_message = {
    "TYPE": "A",
    "NAME": "fibonacci.com"
}

# Send registration message
print("Sending registration message...")
send_udp_message(registration_message)

# Send query message
print("\nSending query message...")
send_udp_message(query_message)
