from socket import *

servername='172.0.0.1'
serverport=12000

clientsocket=socket(AF_INET,SOCK_STREAM)
clientsocket.connect((servername,serverport))

message=input("enter a word: ")
clientsocket.send(message.encode())
modifiedmessage=clientsocket.recv(2048)
print(f"from server: {modifiedmessage.decode()}")
clientsocket.close()
