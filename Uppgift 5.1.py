import socket

class Game:
    def __init__(self, isServer, mySocket):
        self._mySocket = mySocket
        self._isServer = isServer
        self._myScore = 0
        self._OppScore = 0

    def PlayRound(self, myMove, oppMove):
        _myMove = self.makeMoveToNumb(myMove)
        _oppMove = self.makeMoveToNumb(oppMove)

        if _myMove == _oppMove:
            print("You both picked the same move")
        elif _myMove == 3 and _oppMove == 2:
            print("You won the round!")
            self._myScore += 1
        elif _myMove == 2 and _oppMove == 1:
            print("You won the round!")
            self._myScore += 1
        elif _myMove == 1 and _oppMove == 3:
            print("You won the round!")
            self._myScore += 1
        else:
            print("Your opponent won the round.")
            self._OppScore += 1
        
        self.PrintScore()

    def makeMoveToNumb(self, move):
        _move = move.lower()
        if move == "r":
            return 1
        elif move == "p":
            return 2
        elif move == "s":
            return 3

    def PrintScore(self):
        print("Score (you, opponent): {} - {} ".format(self._myScore, self._OppScore))

    def isLegitMove(self, move):
        _move = move.lower()
        if _move is "r" or "p" or "s":
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

            game.PlayRound(myMove, oppMove)

            if game.isOver():
                break


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
                    
        clientSocket.sendall(bytearray(myMove, "ascii"))
        print("Waiting for opponent")
        oppMove = clientSocket.recv(1024)

        game.PlayRound(myMove, oppMove)

        if game.isOver():
                break





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

