# classe de pc pra impotar main
import socket
import threading

class PC:
    def __init__(self, nome, ip, porta, id):
        self.nome = nome
        self.ip = ip
        self.porta = porta
        self.id = id

    def listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.porta))
        self.socket.listen()
        # print(f'{self.nome} escutando...')

        while True:
            con, _ = self.socket.accept()
            msg = con.recv(2048).decode()
            print(f'{self.nome} recebeu: {msg}')
            con.close()
        
    def send(self, msg, ip, porta):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.connect((ip, porta))
        con.send(msg.encode())
        con.close()

