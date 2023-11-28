import socket
import datetime
from time import sleep

def start_client():
    # Impostazioni del client
    host = '127.0.0.1'
    port = 8000

    # Crea un oggetto socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connessione al server
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    while True:
        # Invia dati al server
        value = input("Inserisci il valore della misurazione: ")
        time = datetime.datetime.now()
        measure_time = f"{value}|{time}"
        client_socket.send(f'{measure_time}'.encode())

        # Ricevi la risposta dal server
        response = client_socket.recv(1024)
        print(f"Server response: {response.decode()}")
        sleep(15)

    # Chiudi la connessione con il server
    client_socket.close()

if __name__ == "__main__":
    start_client()