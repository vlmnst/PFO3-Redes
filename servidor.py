import socket
import threading

HOST = '127.0.0.1'
PORT = 5001

def procesar_tarea(conn, addr):
    print(f"[+] Nueva conexión desde {addr}")
    try:
        data = conn.recv(1024).decode('utf-8')
        if data:
            print(f"[*] Tarea recibida de {addr}: {data}")
            # Simulación de procesamiento de la tarea
            resultado = f"OK: Tarea '{data}' procesada con éxito por el servidor."
            conn.sendall(resultado.encode('utf-8'))
    except Exception as e:
        print(f"[-] Error procesando cliente {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Conexión cerrada con {addr}")

def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Servidor Worker escuchando en {HOST}:{PORT}...")

    while True:
        conn, addr = server.accept()
        # Se asigna la atención del cliente a un hilo nuevo (Pool de hilos)
        thread = threading.Thread(target=procesar_tarea, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()