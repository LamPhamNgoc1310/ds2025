# NOTE: the code basically reads the file (as normal) and send to a random address of the client in localhost

import socket

HOST = '127.0.0.1'
PORT = 8080
BUFFER_SIZE = 1024

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server is hosted at: {HOST}:{PORT}")

    client_socket, client_address = server_socket.accept()
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
    main()

