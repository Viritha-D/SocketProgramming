from socket import *
servername='10.12.249.103'
serverport=12000

clientsocket=socket(AF_INET,SOCK_STREAM)
clientsocket.connect((servername,serverport))

msg=input("enter password: ")
clientsocket.send(msg.encode())
respone=clientsocket.recv(2048)
print(f"response:{respone.decode()}")
clientsocket.close()
print("connection is closed")
