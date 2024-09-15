import socket

# Crear un socket de cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))  # Conectar al servidor

# Recibir mensaje del servidor
mensaje = client_socket.recv(1024)
print(f"Mensaje del servidor: {mensaje.decode()}")

# Cerrar la conexión
client_socket.close()
