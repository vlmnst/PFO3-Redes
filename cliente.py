import socket

HOST = '127.0.0.1'
PORT = 5001

def enviar_tarea(descripcion_tarea):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
            print(f"[*] Enviando tarea: '{descripcion_tarea}'")
            client.sendall(descripcion_tarea.encode('utf-8'))
            
            respuesta = client.recv(1024).decode('utf-8')
            print(f"[*] Respuesta del servidor: {respuesta}")
        except ConnectionRefusedError:
            print("[-] No se pudo conectar al servidor. ¿Está ejecutándose servidor.py?")

if __name__ == "__main__":
    tarea = input("Ingresa la tarea a enviar al servidor: ")
    enviar_tarea(tarea)