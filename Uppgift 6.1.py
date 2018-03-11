import socket

def ServerSetup():
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', 80)) #Bind my IP + port
    serverSocket.listen(1)

    print("Listening for clients...")
    (clientSocket, clientAdress) = serverSocket.accept()
    print("Connection from {}".format(clientAdress))


    incoming = clientSocket.recv(1024)
    message = incoming.decode("ascii")

    clientSocket.sendall(bytearray("HTTP/1.1 200 ok\n", "ascii"))
    clientSocket.sendall(bytearray("\n", "ascii"))
    clientSocket.sendall(bytearray("<html>", "ascii"))
    clientSocket.sendall(bytearray("<body>", "ascii"))
    clientSocket.sendall(bytearray("<h1>Your Request</h1>", "ascii"))
    clientSocket.sendall(bytearray("<p>Your client sent this request</p>", "ascii"))
    clientSocket.sendall(bytearray("<pre>{}</pre>".format(message), "ascii"))
    clientSocket.sendall(bytearray("</body>", "ascii"))
    clientSocket.sendall(bytearray("</html>", "ascii"))

    clientSocket.close()    
    print("Client {} disconnected".format(clientAdress))



ServerSetup()