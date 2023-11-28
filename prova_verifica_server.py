import socket
from sys import argv
import threading
import sqlite3

# Configurazione del server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen(5)
print("Server in ascolto...")

# Functions that handles the clients
def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    parti_richiesta = request.split('|')
    request_type = parti_richiesta[0]

    if request_type == 'CHECK_FILE':
        # Verifica la presenza di un file
        file_name = parti_richiesta[1]
        result = check_file_existence(file_name)
        client_socket.send(result.encode())
        
    elif request_type == 'GET_NUM_FRAGMENTS':
        # Ottieni il numero di frammenti di un file
        file_name = parti_richiesta[1]
        result = chek_num_fragments_one_file(file_name)
        client_socket.send(result.encode())
        
    elif request_type == 'GET_HOST_IP':
        # Ottieni l'IP dell'host che ospita un frammento
        fragment_number = parti_richiesta[1]
        result = check_host_of_fragment(fragment_number)
        client_socket.send(result.encode())
        
    elif request_type == 'GET_ALL_HOST_IPS':
        # Ottieni tutti gli IP degli host che ospitano i frammenti di un file
        file_name = parti_richiesta[1]
        result = check_id_of_host_of_fragments(file_name)
        client_socket.send(result.encode())

    else:
        client_socket.send("Invalid request".encode())
    
    client_socket.close()

def check_file_existence(file_name):
     # Esegui la query sul database e restituisci True se il file esiste, altrimenti False
    db_conn = sqlite3.connect('file.db')
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT COUNT(*) FROM files WHERE nome= {file_name}")
    result = db_cursor.fetchone()[0]
    db_conn.close()
    return str(result == 1)

def chek_num_fragments_one_file(file_name):
    # Esegue la query sul database e restituisce il numero di frammenti di un file
    db_conn = sqlite3.connect('file.db')
    db_cursor = db_conn.cursor()
    db_cursor.execute(f"SELECT tot_frammenti FROM files WHERE nome = '{file_name}' ")
    result = db_cursor.fetchone()[0]
    db_conn.close()
    return str(result)

def check_host_of_fragment(fragment_number):
    # Esegue la query sul database e restituisce l'IP dell'HOST che ospita il frammento richiesto
    db_conn = sqlite3.connect('file.db')
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT host FROM frammenti WHERE id_frammento = {fragment_number}")
    result = db_cursor.fetchone()[0]
    db_conn.close()
    return str(result)

def check_id_of_host_of_fragments(file_name):
    # Esegue la query sul database e restituisce l'IP di tutti gli HOST che ospitano i frammenti di un file
    db_conn = sqlite3.connect('file.db')
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT frammenti.host FROM frammenti, files WHERE files.name = {file_name} AND files.id_file = frammenti.id_file")
    result = db_cursor.fetchall
    db_conn.close()
    return str(result)

while True:
    client, addr = server.accept()
    print("Connessione da: " + str(addr))
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()