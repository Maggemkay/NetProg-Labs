import socket

def ServerSetup():
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', 60003))
    serverSocket.listen(1)

    while True:
        print("Listening for clients...")
        (clientSocket, clientAddress) = clientSocket.accept()
        print("Connection from {}".format(clientAddress))

        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            print('Received:', data.decode("ascii"))
            answer = "Thanks for the data!"
            clientSocket.sendall(bytearray(answer, "ascii"))
            print("Answered:", answer)
        clientSocket.close()
        print("Client {} disconnected".format(clientAddress))

def ClientSetup():
    clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    clientSocket.connect(('127.0.0.1', 60003))

    message = input("Type yout message:")
    clientSocket.sendall(bytearray(message, "ascii"))
    print("Sent:", message)

    data = clientSocket.recv(1024)
    print("Received:", data.decode("ascii"))

    clientSocket.close()
