import socket
import threading

# Función para manejar conexiones entrantes (actúa como servidor)
def servidor_p2p():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8081))
    server_socket.listen(1)
    print("Esperando conexión P2P...")

    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")
    client_socket.sendall(b"Mensaje desde el nodo P2P")
    client_socket.close()
    server_socket.close()

# Función para conectarse a otro nodo (actúa como cliente)
def cliente_p2p():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8081))
    mensaje = client_socket.recv(1024)
    print(f"Mensaje de otro peer: {mensaje.decode()}")
    client_socket.close()

# Ejecutar ambas funciones simultáneamente
threading.Thread(target=servidor_p2p).start()
cliente_p2p()
