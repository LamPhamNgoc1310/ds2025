# NOTE: this code basically listens and validates 'chunk' variables from the localhost:8080 and saves (writes) them.

import socket

HOST = '127.0.0.1'
PORT = 8080
BUFFER_SIZE = 1024

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print(f"Client is receiving from server at: {HOST}:{PORT}")

    fileName = 'received_file.txt'
    try:
        with open(fileName, 'wb') as file:
            while True:
                chunk = client_socket.recv(BUFFER_SIZE)
                if not chunk:
                    break # stop when EOF
                file.write(chunk)
                # for f in file:
                #     if not f:
                #         break # stop when EOF
                # file.write(f) # saving file from the server file
        print(f"file is saved as {fileName}")
    except Exception as e:
        print(f"Receiving error: {e}")

    client_socket.close()
    print('Client closed')
if __name__ == "__main__":
    main()