from socket import *
import threading

serverName = '10.12.249.103'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def receive():
    while True:
        try:
            msg = clientSocket.recv(2048).decode()
            if msg:
                print("\n" + msg)
        except:
            break

# Start a thread to receive messages
threading.Thread(target=receive, daemon=True).start()

print("Connected to the chat. Type and press Enter to send.")
while True:
    message = input()
    if message.lower() == 'exit':
        break
    clientSocket.send(message.encode())

clientSocket.close()
