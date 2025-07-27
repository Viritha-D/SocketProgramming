from socket import *
import threading

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('10.12.249.103', serverPort))
serverSocket.listen(2)  # Allow up to 2 queued connections
print("TCP Chat Server is ready to receive on port", serverPort)

clients = []  # To store connected client sockets

def client_handler(clientSocket, clientAddress):
    print(f"Connection accepted from {clientAddress}")
    while True:
        try:
            message = clientSocket.recv(2048).decode()
            if not message:
                break  # Connection closed
            print(f"Received from {clientAddress}: {message}")
            
            # Broadcast the message to the other client
            for other_client in clients:
                if other_client != clientSocket:
                    other_client.send(f"{clientAddress} says: {message}".encode())
        except:
            break
    
    print(f"Connection closed from {clientAddress}")
    clients.remove(clientSocket)
    clientSocket.close()

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    clients.append(connectionSocket)
    
    # Handle this client in a new thread
    threading.Thread(target=client_handler, args=(connectionSocket, clientAddress)).start()
