from socket import *


def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 6000))
        serversocket.listen(5)

        while (True):
            (client_socket, adress) = serversocket.accept()

            coming_request = client_socket.recv(5000).decode()
            pieces = coming_request.split('\n')
            if len(pieces) > 0: print(pieces[0])

            data = "HTTP/1.1 200 OK \r\n"
            data += "Content-Type: text/html charset=utf-8 \r\n"
            data += "\r\n"
            data += "<html><body> Hello World </body></html> \r\n\r\n"

            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)

    except:
        print("Shutting Down the Server")

    serversocket.close()


print("Server is listening localhost:9000")
createServer()
