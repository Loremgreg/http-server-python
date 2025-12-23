import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True) # crée un socket TCP, le bind sur localhost:4221, le met en mode écoute

    # server_socket.accept()[0].sendall(b"HTTP/1.1 200 OK\r\n\r\n")
        # 1. Attendre une connexion (bloquant)
    client_socket, _ = server_socket.accept()

    # 2. Envoyer la réponse HTTP exacte attendue
    client_socket.sendall(b"HTTP/1.1 200 OK\r\n\r\n")

    # 3. Fermer proprement
    client_socket.close()
    server_socket.close()
    
    # server_socket.accept()  # wait for client

if __name__ == "__main__":
    main()
