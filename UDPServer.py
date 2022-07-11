from socket import *
serverPort = 54321
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))
print("The server is ready to receive")


while True:
    data, clientAddress = serverSocket.recvfrom(4096)
    modifiedData = data.decode().upper()
    serverSocket.sendto(modifiedData.encode(), clientAddress)
