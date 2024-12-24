import socket

HOST = '0.0.0.0'
PORT = 8080
BUFFER_SIZE = 1024

def start_server():
    sv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sv_sock.bind(HOST, PORT)
    sv_sock.listen(1)
    print(f"Server is listening at {HOST}:{PORT}")

    client_socket, client_address = sv_sock.accept()
    print(f"Connection with {client_address}")

    fileName = 'sent_file.txt'
    try:
        with open(fileName, 'rb') as file:
            while chunk := file.read(BUFFER_SIZE):
                client_socket.sendall(chunk) # sending file to the client
            print(f"Reading {fileName}")

    except Exception as e:
        print(f"sending error: {e}")

    client_socket.close()
    server_socket.close()
    print('Server closed')

if __name__ == "__main__":
    start_server()