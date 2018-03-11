import socket
import select

port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(2)

listOfSockets = [sockL]

print("Listen on port {}".format(port))

while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockL:
        (sockClient, addr) = sockL.accept()
        listOfSockets.append(sockClient)
        connectMessage = "[{}] Connected".format(sockClient.getpeername())
        print("{} Connected".format(sockClient.getpeername()))
        for clients in listOfSockets:
            if clients != sockL:
                clients.sendall(bytearray(connectMessage, "ascii"))
    else:
        data = sock.recv(2048)
        if not data:
            disconnectMessage = "[{}] Disconnected".format(sockClient.getpeername())
            print("{} Disconnected".format(sockClient.getpeername()))
            for clients in listOfSockets:
                if clients != sockL:
                    clients.sendall(bytearray(disconnectMessage, "ascii"))
            sock.close()
            listOfSockets.remove(sock)
        else:
            message = "[{}]: ".format(sock.getpeername()) + data.decode("ascii")
            for clients in listOfSockets:
                if clients != sockL:
                    clients.sendall(bytearray(message, "ascii"))

