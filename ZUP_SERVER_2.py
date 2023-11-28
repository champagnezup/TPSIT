import socket as sck
import sqlite3 
from threading import Thread


class Client(Thread):
    def __init__(self, id, conn: sck.socket, addr):
        Thread.__init__(self)
        self.id = id
        self.conn = conn
        self.addr = addr

    def run(self):
        station_id = self.id

        while True:
            # Ricevi dati dal client
            request = client_socket.recv(1024).decode()
            parti_richiesta = request.split('|')
            measured_level = parti_richiesta[0]
            time = parti_richiesta[1]

            # Eseguo le query sul database per ottenere: il nome della localita, il nome del fiume e il livello di guardia
            db_conn = sqlite3.connect('fiumi.db')
            db_cursor = db_conn.cursor()
            db_cursor.execute(
                f"SELECT livello from livelli where id_stazione = {station_id}")
            local_level = db_cursor.fetchone()[0]
            db_conn.close()

            db_conn = sqlite3.connect('fiumi.db')
            db_cursor = db_conn.cursor()
            db_cursor.execute(
                f"SELECT fiume from livelli where id_stazione = {station_id}")
            river = db_cursor.fetchone()[0]
            db_conn.close()

            db_conn = sqlite3.connect('fiumi.db')
            db_cursor = db_conn.cursor()
            db_cursor.execute(
                f"SELECT localita from livelli where id_stazione = {station_id}")
            locality = db_cursor.fetchone()[0]
            db_conn.close()

            # Invia una risposta al client in base al livello misurato
            if (float(measured_level) / float(local_level)) * 100 < 30:
                response = "Ricezione dati"
                client_socket.send(response.encode())
                print(
                    f"località: {locality}, fiume: {river}, ora: {time}, NIENTE DA SEGNALARE")
            elif (float(measured_level) / float(local_level)) * 100 >= 30 and (float(measured_level) / float(local_level)) * 100 < 70:
                response = "Ricezione dati"
                client_socket.send(response.encode())
                print(
                    f"località: {locality}, fiume: {river}, ora: {time}, AVVISO PERICOLO IMMINENTE!")
            elif (float(measured_level) / float(local_level)) * 100 > 70:
                response = "Ricezione dati, AVVIARE ALLARME!"
                client_socket.send(response.encode())
                print(
                    f"località: {locality}, fiume: {river}, ora: {time}, AVVISO PERICOLO INCORSO!")

# Impostazioni del server
host = '127.0.0.1'
port = 8000
# Crea un oggetto socket
server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
# Associa il socket all'host e alla porta desiderati
server.bind((host, port))

n_cl = 1
while True:
    # Metti il socket in ascolto
    server.listen()
    print(f"Server listening on {host}:{port}")
     # Accetta la connessione del client
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")
    # Crea un thread per gestire la connessione del client
    cl = Client(n_cl, client_socket, addr)
    cl.start()
    n_cl += 1

server.close()
