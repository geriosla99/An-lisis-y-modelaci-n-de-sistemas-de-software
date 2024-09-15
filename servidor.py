import socket

# Crear un socket de servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))  # Asignar dirección y puerto
server_socket.listen(1)  # Escuchar conexiones entrantes

print("Servidor escuchando en el puerto 8080...")

# Aceptar conexión del cliente
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con {client_address}")

# Enviar un mensaje al cliente
client_socket.sendall(b"Hola desde el servidor")

# Cerrar la conexión
client_socket.close()
server_socket.close()
