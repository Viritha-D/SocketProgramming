from socket import *

serverport=12000

serversocket=socket(AF_INET,SOCK_STREAM)
serversocket.bind(('10.12.249.123',serverport))
serversocket.listen(1)

print('tcp server is ready to receieve on the port',serverport)

password='v3108'
def checkpass(word):
    if word==password:
        return 'access granted'
    else:
        return 'wrong password'
while True:
    connectsocket,clientaddress=serversocket.accept()
    print(f"connection is established for {clientaddress}")

    msg=connectsocket.recv(2048)
    password1=msg.decode()
    ans=checkpass(password1)
    print(f"response:{ans}")
    connectsocket.send(ans.encode())
    connectsocket.close()
    print("connection is closed")
    
    
