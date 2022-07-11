from socket import *
serverName = '127.0.0.1'
serverPort = 8781
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence :')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("from Server : ", modifiedSentence.decode())
clientSocket.close()