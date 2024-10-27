import socket
import argparse
import threading
import os

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        self.clients = {}  # To store clients' addresses and usernames
        print(f"Server is listening at {self.host}:{self.port}")


    def start(self):
        print("Waiting for messages...")
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
                message = data.decode('ascii')

                if message.startswith('LOGIN'):
                    _, username, password = message.split(maxsplit=2)
                    if username in self.clients.values():
                        self.sock.sendto('Username already taken. Please choose another one.'.encode('ascii'), addr)
                    elif password != 'labschool':
                        self.sock.sendto('Invalid password. Please try again.'.encode('ascii'), addr)
                    else:
                        self.clients[addr] = username
                        self.sock.sendto(f'Welcome {username}!'.encode('ascii'), addr)
                        print(f'{username} has joined from {addr}.')
                else:
                    username = self.clients.get(addr, 'Unknown')
                    print(f'Received message from {username} at {addr}: {message}')
                    self.broadcast(message, addr)
            except Exception as e:
                print(f'An error occurred: {e}')

    def broadcast(self, message, sender_addr):
        for addr in self.clients:
            if addr != sender_addr:
                self.sock.sendto(message.encode('ascii'), addr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDP Chatroom Server")
    parser.add_argument('host', help='The host IP address')
    parser.add_argument('-p', metavar='PORT', type=int, default=8080, help='Port number')
    args = parser.parse_args()
    server = Server(args.host, args.p)
    server.start()



