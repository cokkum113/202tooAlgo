from socket import *
serverName = '127.0.0.1'
serverPort = 54321

clientSocket = socket(AF_INET, SOCK_DGRAM)

data = input('Input lowercase sentence : ')
clientSocket.sendto(data.encode(), (serverName, serverPort))

modifiedData, serverAddress = clientSocket.recvfrom(4096)
print(modifiedData.decode())
clientSocket.close()
