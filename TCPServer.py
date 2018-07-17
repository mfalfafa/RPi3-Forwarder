from socket import *

# Socket Server Initialization
serverPort = 2010
serverSocket = socket(AF_INET, SOCK_STREAM)
# IP of PC Server
serverIP = '169.254.148.241'
serverSocket.bind((serverIP,serverPort))
serverSocket.listen(1)

print 'Server is ready to receive data.'

try:
    while 1:
        # Accept connection from client
        connectionSocket, addr = serverSocket.accept()
        #print(connectionSocket.getpeername())

        # Receives message from Socket Client
        msg=connectionSocket.recv(1024)
        print msg

        # Sends ACK message to Client
        connectionSocket.send('ack')
        while 1:
            msg=connectionSocket.recv(32)
            if msg=='ok':
                connectionSocket.close()
                #serverSocket.close()
                break
except KeyboardInterrupt:
    print 'Connection is closed!'
    connectionSocket.send('closed')
    connectionSocket.close()
    #serverSocket.close()
except Exception as e:
    connectionSocket.close()
    print 'Error : '+ str(e)
