import socket

def enviar_datos(host, port, datos):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((host, port))
        cliente.sendall(datos.encode())  # Enviar datos codificados como bytes

if __name__ == "__main__":
    HOST = '127.0.0.1'  # localhost
    PORT = 65432  # Puerto al que el servidor está escuchando

    # Datos que se enviarán al servidor
    datos = "89958403|Hola, servidor! ¿Cómo estás?"
    datos2 ="59506054|ola"

    enviar_datos(HOST, PORT, datos)
