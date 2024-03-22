"""The client class is used to communicate with the server."""

import socket
import threading
import json

class Client:
    def __init__(self, server_ip, server_port):
        self.last_received = {}
        self.id_ = None
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        threading.Thread(target=self.receive).start()

    def send(self, data):
        data['id'] = self.id_
        json_data = json.dumps(data)
        self.client_socket.send(json_data.encode())

    def receive(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    json_data = json.loads(data.decode())
                    if json_data['header'] == 'new_id':
                        self.id_ = json_data['content']
                    self.last_received = json_data
            except Exception as e:
                print("Error receiving data:", e)
                break

    def close(self):
        self.client_socket.close()

    def __del__(self):
        self.close()

if __name__ == '__main__':
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 12345

    client = Client(SERVER_IP, SERVER_PORT)

    for i in range(100):
        message = input("Enter message to send to server: ")
        client.send({'header' : "test","content": message})
    client.close()