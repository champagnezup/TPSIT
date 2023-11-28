import socket
import threading
import sqlite3

# Configurazione del database SQLite
db_conn = sqlite3.connect('file.db')
db_cursor = db_conn.cursor()

# Funzione per gestire le richieste dei client
def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    parts = request.split('|')
    request_type = parts[0]

    if request_type == 'CHECK_FILE':
        # Verifica la presenza di un file
        file_name = parts[1]
        result = check_file_existence(file_name)
        client_socket.send(result.encode())
    elif request_type == 'GET_NUM_FRAGMENTS':
        # Ottieni il numero di frammenti di un file
        file_name = parts[1]
        num_fragments = get_num_fragments(file_name)
        client_socket.send(str(num_fragments).encode())
    elif request_type == 'GET_HOST_IP':
        # Ottieni l'IP dell'host che ospita un frammento
        file_name = parts[1]
        fragment_number = int(parts[2])
        host_ip = get_host_ip(file_name, fragment_number)
        client_socket.send(host_ip.encode())
    elif request_type == 'GET_ALL_HOST_IPS':
        # Ottieni tutti gli IP degli host che ospitano i frammenti di un file
        file_name = parts[1]
        host_ips = get_all_host_ips(file_name)
        client_socket.send('|'.join(host_ips).encode())
    else:
        client_socket.send("Invalid request".encode())

    client_socket.close()

# Funzione per verificare la presenza di un file
def check_file_existence(file_name):
    # Esegui la query sul database e restituisci True se il file esiste, altrimenti False
    db_cursor.execute("SELECT COUNT(*) FROM files WHERE nome=?", (file_name,))
    result = db_cursor.fetchone()[0]
    return str(result == 1)

# Funzione per ottenere il numero di frammenti di un file
def get_num_fragments(file_name):
    # Esegui la query sul database e restituisci il numero di frammenti
    db_cursor.execute("SELECT tot_frammenti FROM files WHERE nome=?", (file_name,))
    result = db_cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

# Funzione per ottenere l'IP dell'host che ospita un frammento di un file
def get_host_ip(file_name, fragment_number):
    # Esegui la query sul database e restituisci l'IP dell'host
    db_cursor.execute("SELECT host FROM frammenti WHERE id_file=(SELECT id_file FROM files WHERE nome=?) AND n_frammento=?", (file_name, fragment_number))
    result = db_cursor.fetchone()
    if result:
        return result[0]
    else:
        return "Host non trovato"

# Funzione per ottenere tutti gli IP degli host che ospitano i frammenti di un file
def get_all_host_ips(file_name):
    # Esegui la query sul database e restituisci una lista di IP
    db_cursor.execute("SELECT host FROM frammenti WHERE id_file=(SELECT id_file FROM files WHERE nome=?)", (file_name,))
    results = db_cursor.fetchall()
    return [result[0] for result in results]

# Configurazione del server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9090))
server.listen(5)
print("Server in ascolto...")

while True:
    client, addr = server.accept()
    print("Connessione da: " + str(addr))
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
