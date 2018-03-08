import socket

class Game:
    def __init__(self, isServer, mySocket):
        self._mySocket = mySocket
        self._isServer = isServer
        self._myScore = 0
        self._OppScore = 0

    def PlayRound(self, myMove, oppMove):
        _myMove = makeMoveToNumb(myMove)
        _oppMove = makeMoveToNumb(oppMove)

        if _myMove == _oppMove:
            print("You both picked the same move")
        elif _myMove == 3 and _oppMove == 2:
            print("You won the round!")
            self._myScore++
        elif _myMove == 2 and _oppMove == 1:
            print("You won the round!")
            self._myScore++
        elif _myMove == 1 and _oppMove == 3:
            print("You won the round!")
            self._myScore++
        else:
            print("Your opponent won the round.")
            self._OppScore++
        
        PrintScore()

    def makeMoveToNumb(self, move)
        _move = move.lower()
        if move == "r":
            return 1
        elif move == "p":
            return 2
        elif move == "s":
            return 3

    def PrintScore(self):
        print("Score (you, opponent): {} - {} ".format(self._myScore, self._OppScore))

    def isLegitMove(self, move)
        _move = move.lower()
        if _move is not "r" or "p" or "s":
            return False
        else:
            return True


        

def ServerSetup():
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', 60003)) #Bind my IP + port
    serverSocket.listen(1)

    while True:
        print("Listening for clients...")
        (clientSocket, clientAddress) = serverSocket.accept()
        print("Connection from {}".format(clientAddress))

        #The Game
        game = Game(True, serverSocket)

        while True:
            print("Waiting for opponent")
            oppMove = clientSocket.recv(1024)

            while True:
                myMove = input("Your move: ")
                if game.isLegitMove(myMove):
                    break
                else:
                    print("Not a valid move, try again")

            clientSocket.sendall(bytearray(message, "ascii"))

            game.PlayRound(myMove, oppMove)


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
    clientSocket.connect(('127.0.0.1', 60003)) #Connect to this server

    #The Game
    game = Game(False, clientSocket)

    while True:
        while True:
                myMove = input("Your move: ")
                if game.isLegitMove(myMove):
                    break
                else:
                    print("Not a valid move, try again")
                    
        clientSocket.sendall(bytearray(message, "ascii"))
        print("Waiting for opponent")
        oppMove = clientSocket.recv(1024)

        game.PlayRound(myMove, oppMove)

        





        # message = input("Type yout message:")
        # clientSocket.sendall(bytearray(message, "ascii"))
        # print("Sent:", message)

        # data = clientSocket.recv(1024)
        # print("Received:", data.decode("ascii"))

    clientSocket.close()


print("Welcome to rock, paper, scissors!")
while True:
    answer = input("Do you want to be client or server (C/S): ")
    if (answer == "C" or answer == "c"):
        print("When it´s your turn, pick R/P/S.")
        ClientSetup()
        break
    elif(answer == "S" or answer == "s"):
        print("When it´s your turn, pick R/P/S.")
        ServerSetup()
        break
    else:
        print("Wrong input, try again")


# class Card:
    
#     suiteStr = { 1: "Härter", 
#                 2: "Ruter",
#                 3: "Spader",
#                 4: "Klöver"
#                 }

#     valueStr = {
#                 1: "Äss",
#                 2: "Två",
#                 3: "Tre",
#                 4: "Fyra",
#                 5: "Fem",
#                 6: "Sex",
#                 7: "Sju",
#                 8: "Åtta",
#                 9: "Nio",
#                 10: "Tio",
#                 11: "Knekt",
#                 12: "Dam",
#                 13: "Kung"
#                 }

#     def __init__(self, suite, value):
#         assert 1 <= suite <= 4 and 1 <= value <= 13
#         self._suite = suite
#         self._value = value

#     def getValue(self):
#         return self._value

#     def getSuite(self):
#         return self._suite
        
#     def __str__(self):
#         return self.suiteStr[self._suite] + " " + self.valueStr[self._value]