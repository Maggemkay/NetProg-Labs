import socket

class Game:
    def __init__(self, isServer, mySocket):
        self._mySocket = mySocket
        self._isServer = isServer
        self._myScore = 0
        self._OppScore = 0

    def PlayRound(self, thisPC, otherPC):

        _p1 = thisPC.lower()
        _p2 = otherPC.lower()

        if _p1 == _p2:
            print("You both picked the same move")
        elif _p1 == "r" and _p2 == "s":
            print("You won the round!")
            self._myScore += 1
        elif _p1 == "p" and _p2 == "r":
            print("You won the round!")
            self._myScore += 1
        elif _p1 == "s" and _p2 == "p":
            print("You won the round!")
            self._myScore += 1
        else:
            print("Your opponent won the round.")
            self._OppScore += 1
        
        self.PrintScore()

    def PrintScore(self):
        print("Score (you, opponent): {} - {} ".format(self._myScore, self._OppScore))

    def isLegitMove(self, move):
        _move = move.lower()
        if _move == "r" or _move == "p" or _move == "s":
            return True
        else:
            return False

    def isOver(self):
        if self._myScore == 10:
            print("You won {} to {}".format(self._myScore, self._OppScore))
            return True
        elif self._OppScore == 10:
            print("You lost {} to {}".format(self._myScore, self._OppScore))
            return True
        else:
            return False


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
        print("When it´s your turn, pick R/P/S.")

        while True:
            print("Waiting for opponent")
            oppMove = clientSocket.recv(1024)

            while True:
                myMove = input("Your move: ")
                if game.isLegitMove(myMove):
                    break
                else:
                    print("Not a valid move, try again")

            clientSocket.sendall(bytearray(myMove, "ascii"))

            game.PlayRound(myMove, oppMove.decode("ascii"))

            if game.isOver():
                break

        clientSocket.close()
        print("Client {} disconnected".format(clientAddress))



def ClientSetup(serverIP):
    clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    clientSocket.connect((serverIP, 60003)) #Connect to this server

    #The Game
    game = Game(False, clientSocket)
    print("When it´s your turn, pick R/P/S.")

    while True:
        while True:
            myMove = input("Your move: ")
            if game.isLegitMove(myMove):
                break
            else:
                print("Not a valid move, try again")
                    
        clientSocket.sendall(bytearray(myMove, "ascii"))
        print("Waiting for opponent")
        oppMove = clientSocket.recv(1024)

        game.PlayRound(myMove, oppMove.decode("ascii"))

        if game.isOver():
                break

    clientSocket.close()


print("Welcome to rock, paper, scissors!")
while True:
    answer = input("Do you want to be client or server (C/S): ")
    if (answer == "C" or answer == "c"):
        serverIP = input("The server IP: ")
        ClientSetup(serverIP)
        break
    elif(answer == "S" or answer == "s"):
        ServerSetup()
        break
    else:
        print("Wrong input, try again")
