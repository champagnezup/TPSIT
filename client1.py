#192.168.1.130
import socket #nativa
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #costruttore --> con questa riga ho istanziato il socket (creazione del socket)
server_address = ('192.168.1.133', 3450) #192.168.0.123 indirizzo IP alphabot
s.connect(server_address)
print("connesso")

class receiver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.connection=s
    
    def run(self):
        while True:
            text_received, address = s.recvfrom(4096)
            print(text_received.decode())

def main():
    ricevitore=receiver()
    ricevitore.start()
    while True:
        text = input("Scrivi il nome del comando(F, B, L, R, E): ")+ ";"+ input("inserisci la durata': ")+","+input("inserisci la velocità: ")
        #print(text)
        s.sendto(text.encode(), server_address) #mando il messaggio al server
        text_received, address = s.recvfrom(4096)
        print(text_received.decode())
        if(text_received.decode()=="exit"): break

    s.close()


if __name__ == "__main__":
    main()