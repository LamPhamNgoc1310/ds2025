import socket

SERVER_IP = '127.0.0.1'  # Change to the server's IP if not local
PORT = 12345
BUFFER_SIZE = 1024

def send_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, PORT))
        print(f"Connected to server at {SERVER_IP}:{PORT}")

        with open(filename, "rb") as file:
            while (chunk := file.read(BUFFER_SIZE)):
                client_socket.sendall(chunk)
        
        print("File sent successfully.")

if __name__ == "__main__":
    send_file("file_to_send.txt")
