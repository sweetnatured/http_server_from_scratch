from socket import *

def respond_header(status_code:int):
    header = ""
    if status_code == 200:
        header = f"HTTP/1.1 {status_code} \n"
        header += "Content-Type: text/html charset=utf-8 \n"
        header += "\r\n"

    if status_code == 404:
        header += f"HTTP/1.1 {status_code} Not Found \n"
        header += "Content-Type: text/html charset=utf-8 \n"
        header += "\r\n"
        header += "<html><body> <h1>404 Page is not found</h1> </body></html> \n\n"

    return header


def respond_data(html_file:str, header) -> str:

    data = header

    with open(html_file) as html:
        html_as_string = html.read()
        data += f"{html_as_string} \n\n"

    return data


def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9412))
        serversocket.listen(5)

        while (True):
            (client_socket, adress) = serversocket.accept()

            coming_request = client_socket.recv(5000).decode()
            request_method = coming_request.split(' ')[0]

            data = ""
            if request_method == "GET" or request_method == "HEAD":

                file_requested = coming_request.split(' ')[1]

                if file_requested == "/":
                    header = respond_header(200)
                    file_requested = "index.html"
                    data = respond_data(file_requested , header)
                else:
                    data = respond_header(404)

            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)

    except:
        print("Shutting Down the Server")
        serversocket.close()


print("Server is listening localhost:9000")
createServer()
