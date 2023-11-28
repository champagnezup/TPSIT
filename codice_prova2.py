import socket

# Funzione per inviare una richiesta al server
def send_request(request):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9090))
    client.send(request.encode())
    response = client.recv(1024).decode()
    print("Risposta dal server: " + response)
    client.close()

while True:
    print("Scegli un'azione:")
    print("1. Verifica la presenza di un file")
    print("2. Ottieni il numero di frammenti di un file")
    print("3. Ottieni l'IP dell'host che ospita un frammento")
    print("4. Ottieni tutti gli IP degli host che ospitano i frammenti di un file")
    choice = input("Inserisci il numero dell'azione desiderata: ")

    if choice == '1':
        file_name = input("Inserisci il nome del file da verificare: ")
        send_request(f'CHECK_FILE|{file_name}')
    elif choice == '2':
        file_name = input("Inserisci il nome del file: ")
        send_request(f'GET_NUM_FRAGMENTS|{file_name}')
    elif choice == '3':
        file_name = input("Inserisci il nome del file: ")
        fragment_number = input("Inserisci il numero del frammento: ")
        send_request(f'GET_HOST_IP|{file_name}|{fragment_number}')
    elif choice == '4':
        file_name = input("Inserisci il nome del file: ")
        send_request(f'GET_ALL_HOST_IPS|{file_name}')
    else:
        print("Scelta non valida")
