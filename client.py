import threading
import socket
import argparse
import sys
import tkinter as tk

class Send(threading.Thread):
    def __init__(self, sock, name, host, port):
        super().__init__()
        self.sock = sock
        self.name = name
        self.host = host
        self.port = port

    def run(self):
        while True:
            message = input(f'{self.name}: ')
            if message == "QUIT":
                self.sock.sendto(f'{self.name} has left the chat.'.encode('ascii'), (self.host, self.port))
                print('\nQuitting...')
                self.sock.close()
                sys.exit(0)
            else:
                self.sock.sendto(f'{self.name}: {message}'.encode('ascii'), (self.host, self.port))

class Receive(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock
        self.messages = None

    def run(self):
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
                message = data.decode('ascii')
                print(f'\r{message}\n', end='')

                if self.messages:
                    self.messages.insert(tk.END, message)
            except OSError:
                break

class Client:
    def __init__(self, host, server_port, client_port):
        self.host = host
        self.server_port = server_port
        self.client_port = client_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', client_port))
        self.name = None
        self.messages = None

    def start(self):
        print(f'Trying to connect to {self.host}:{self.server_port} using UDP on client port {self.client_port}...')
        while True:
            self.name = input('Username: ')
            self.password = input('Password: ')
            self.sock.sendto(f'LOGIN {self.name} {self.password}'.encode('ascii'), (self.host, self.server_port))
            response, _ = self.sock.recvfrom(1024)
            response_message = response.decode('ascii')

            if response_message == 'Username already taken. Please choose another one.':
                print(response_message)
                continue  # Ask for username again
            elif response_message == 'Invalid password. Please try again.':
                print(response_message)
                continue  # Ask for password again
            else:
                print(response_message)
                break

        print('Getting ready to send and receive messages...')
        
        send = Send(self.sock, self.name, self.host, self.server_port)
        receive = Receive(self.sock)
        send.start()
        receive.start()
        
        self.sock.sendto(f'{self.name} has joined the chat.'.encode('ascii'), (self.host, self.server_port))
        print("\rReady! Leave the chatroom anytime by typing 'QUIT'\n")
        print(f'{self.name}: ', end='')
        
        return receive

    def send(self, textInput):
        message = textInput.get()
        textInput.delete(0, tk.END)
        self.messages.insert(tk.END, f'{self.name}: {message}')
        if message == "QUIT":
            self.sock.sendto(f'{self.name} has left the chat.'.encode('ascii'), (self.host, self.server_port))
            print('\nQuitting...')
            self.sock.close()
            sys.exit(0)
        else:
            self.sock.sendto(f'{self.name}: {message}'.encode('ascii'), (self.host, self.server_port))

def main(host, server_port, client_port):
    client = Client(host, server_port, client_port)
    receive = client.start()

    window = tk.Tk()
    window.title("Labschool Bos Roomchat")

    fromMessage = tk.Frame(master=window)
    scrollBar = tk.Scrollbar(master=fromMessage)
    messages = tk.Listbox(master=fromMessage, yscrollcommand=scrollBar.set)
    scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
    messages.pack(side=tk.LEFT, fill=tk.BOTH)
    
    client.messages = messages
    receive.messages = messages

    fromMessage.grid(row=0, column=0, columnspan=2, sticky="nsew")
    fromEntry = tk.Frame(master=window)
    textInput = tk.Entry(master=fromEntry)

    textInput.pack(fill=tk.BOTH)
    textInput.bind("<Return>", lambda x: client.send(textInput))
    textInput.insert(0, "Write your message here.")

    btnSend = tk.Button(master=window, text='Send', command=lambda: client.send(textInput))
    fromEntry.grid(row=1, column=0, padx=10, sticky="ew")
    btnSend.grid(row=1, column=1, pady=10, sticky="ew")

    window.rowconfigure(0, minsize=500, weight=1)
    window.rowconfigure(1, minsize=50)
    window.columnconfigure(0, minsize=500)
    window.columnconfigure(1, minsize=200)

    window.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="UDP Chatroom Client")
    parser.add_argument('host', help='The host IP address')
    parser.add_argument('server_port', type=int, help='Server port number')
    parser.add_argument('client_port', type=int, help='Client port number')
    args = parser.parse_args()
    main(args.host, args.server_port, args.client_port)

