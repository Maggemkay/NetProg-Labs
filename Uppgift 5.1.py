import socket

class Game:
    def Game(self, isServer):
        self._isServer = isServer
        self._myScore = 0
        self._OpponentScore = 0

        # if _isServer == True:
    
    def WaitForPlayer():
        pass

    def MyTurn():
        pass

    def PrintScore():
        pass


        

def ServerSetup():
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', 60003))
    serverSocket.listen(1)

    while True:
        print("Listening for clients...")
        (clientSocket, clientAddress) = serverSocket.accept()
        print("Connection from {}".format(clientAddress))

        #The Game
        game = Game(isServer = True)

        while True:






            print("Other players turn...")
            move = clientSocket.recv(1024)
            if not data:
                break
            print("Your turn!")
            
            # data = clientSocket.recv(1024)
            # if not data:
            #     break
            # print('Received:', data.decode("ascii"))
            # answer = "Thanks for the data!"
            # clientSocket.sendall(bytearray(answer, "ascii"))
            # print("Answered:", answer)
        clientSocket.close()
        print("Client {} disconnected".format(clientAddress))



def ClientSetup():
    clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    clientSocket.connect(('127.0.0.1', 60003))

    while True:
        # message = input("Type yout message:")
        # clientSocket.sendall(bytearray(message, "ascii"))
        # print("Sent:", message)

        # data = clientSocket.recv(1024)
        # print("Received:", data.decode("ascii"))

    clientSocket.close()


print("Welcome to sten, sax, påse!")
while True:
    answer = input("Do you want to be client or server (C/S): ")
    if (answer == "C" or answer == "c"):
        ClientSetup()
        break
    elif(answer == "S" or answer == "s"):
        ServerSetup()
        break
    else:
        print("Wrong input, try again")


