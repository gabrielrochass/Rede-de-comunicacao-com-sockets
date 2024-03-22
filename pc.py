# classe de pc pra impotar main
# classe de pc pra impotar main
import socket
import threading
import rsa

class PC:
    def __init__(self, nome, ip, porta, id):
        self.nome = nome
        self.ip = ip
        self.porta = porta
        self.id = id

    def set_key(self, key):
        self.key = key
        return self.key
    
    def send_encrypted(self, msg, ip, porta, id, ca):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        chave_publica_dest = ca.consultar_chave_publica(id)
        text = rsa.encrypt(msg.encode(), chave_publica_dest)
        con.connect((ip, porta))
        con.send(text)
        con.close()

    def listen_encrypted(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.porta))
        self.socket.listen()
        # print(f'{self.nome} escutando...')

        while True:
            con, _ = self.socket.accept()
            msg = con.recv(2048)
            decrypted_msg = rsa.decrypt(msg, self.key)
            print(f'{self.nome} recebeu: {decrypted_msg.decode()}')
            con.close()

        
