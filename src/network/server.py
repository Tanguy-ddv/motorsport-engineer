"""The server class is used to communicate with the clients."""

import socket
import threading
import json

class Server:
    def __init__(self, host_ip, host_port):

        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_sockets = []
        self.__running = True
        self.__last_received = {}
        self.__is_triggered = False
        print(f"server launched: {host_ip}, {host_port}")
        self.__server_socket.bind((host_ip, host_port))
        self.__server_socket.listen(12)
        threading.Thread(target=self.__accept_clients).start()

    def __accept_clients(self):
        while self.__running:
            client_socket, address = self.__server_socket.accept()
            self.__client_sockets.append(client_socket)
            print(f"new client connected: {address} has the id {len(self.__client_sockets)}")
            welcome_message = {"header" : "new_id", "content" : len(self.__client_sockets)}
            json_message = json.dumps(welcome_message)
            client_socket.send(json_message.encode())
            threading.Thread(target=self.__handle_client, args=(client_socket,)).start()

    def __handle_client(self, client_socket: socket.socket):
        while self.__running:
            try:
                data = client_socket.recv(1024)
                if data:
                    json_data = json.loads(data.decode())
                    self.__last_received = json_data
                    self.__is_triggered = True
                else:
                    self.__is_triggered = False
            except Exception as e:
                print("Error handling client data:", e)
                self.__client_sockets.remove(client_socket)
                client_socket.close()
                break
    
    def get_last_received(self) -> dict:
        """Return the last data received."""
        if self.__is_triggered:
            self.__is_triggered = False
            return self.__last_received

    def send(self, client_id, data):
        """The data to one client."""
        if 0 < client_id <= len(self.__client_sockets):
            client_socket = self.__client_sockets[client_id - 1]
            json_data = json.dumps(data)
            client_socket.send(json_data.encode())

    def send_all(self, data):
        """Send data to all the clients."""
        for client_socket in self.__client_sockets:
            json_data = json.dumps(data)
            client_socket.send(json_data.encode())

    def stop(self):
        self.__running = False
        self.__client_sockets.close()
        for client_socket in self.__client_sockets:
            client_socket.close()

if __name__ == '__main__':
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 12345
    server = Server(SERVER_IP, SERVER_PORT)
    while True:
        last_received = server.get_last_received()
        if last_received:
            print(last_received)