import socket
import socket as sck
import AlphaBot
import time
from threading import Thread
import sqlite3

SEPARATOR = ';'

# creazione socket tcp server
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
# creazione istanza AlphaBot
r = AlphaBot.AlphaBot()


class ThreadLed(Thread):
    def __init__(self, connessione):
        super().__init__()
        self.connessione = connessione

    def run(self):
        last_sensor_data = ""
        while True:
            sensor_data = f'{r.getSensoLeft()}{SEPARATOR}{r.getSensoRight()}'
            if sensor_data != last_sensor_data:
                self.connessione.sendall(sensor_data.encode())
                print(sensor_data)
                last_sensor_data = sensor_data
            time.sleep(1)


class ThreadMess(Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def run(self):
        last_sensor_data = ""
        while True:
            sensor_data = f"{r.getDataSensors()}"
            if sensor_data != last_sensor_data:
                self.conn.sendall(sensor_data.encode())
                last_sensor_data = sensor_data
            time.sleep(2)


message_robot = f"{r.getDataSensors()}".encode()
conn.sendall(message_robot)
time.sleep(2)


def main():
    # bind
    address = ('0.0.0.0', 5000)
    s.bind(address)
    s.listen()

    connesione, clientAddress = s.accept()

    thread = ThreadLed(connesione)
    thread.start()
    tmess = ThreadMess(connesione)
    tmess.start()

    while True:
        mex = connesione.recv(4096).decode()  # mex decodificato in ascii

        command1 = mex
        connex = sqlite3.connect("DBalphaBOT.db")
        cursor = connex.cursor()

        res = cur.execute(
            f"SELECT MOV_SEQUENCE FROM MOVEMENTS WHERE SHORTCUT = {command1}")
        movement = res.fetchone()

        commands = movement.split(";")

        com = ""
        duration = ""

        for command in commands:
            for char in command:
                if char.isalpha():
                    com += char
                elif char.isnumeric():
                    duration += char
            if com.lower() == 'b':
                r.backward()
                time.sleep(duration)
                r.stop()
            elif com.lower() == 'f':
                r.forward()
                time.sleep(duration)
                r.stop()
            elif com.lower() == 'r':
                r.right()
                time.sleep(duration)
                r.stop()
            elif com.lower() == 'l':
                r.left()
                time.sleep(duration)
                r.stop()
            elif com.lower() == 'e':
                break
            else:
                print('error')

    message_robot = f"{r.getDataSensors()}".encode()
    connessione.sendall(message_robot)

    connesione.close()
    s.close()


if __name__ == '__main__':
    main()
