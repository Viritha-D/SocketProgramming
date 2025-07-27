from socket import *
serverport=12000
serversocket=socket(AF_INET,SOCK_STREAM)
serversocket.bind(('',serverport))
serversocket.listen(1)
print(f"tcp server is ready to receieve on the port {serverport}")

while True:
    clientaddress,connectionsocket=serversocket.accept()
    print(f"connection accepted from {clientaddress}")

    message=connectionsocket.recv(2048)

    print(f"message receieved is:{message.decode()}")

    modifiedmessage=message.decode().upper()

    connectionsocket.send(modifiedmessage.encode())

    print(f"sent: {modifiedmessage}")

    connectionsocket.close()
