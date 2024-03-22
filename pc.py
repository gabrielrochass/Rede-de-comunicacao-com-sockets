# classe de pc pra impotar main
import socket
import threading
import rsa
from ca import AutoridadeCertificadora

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
            ciphertext = rsa.decrypt(msg,self.key)
            print(f'{self.nome} recebeu: {ciphertext.hex()}')
            con.close()
        
    def send(self, msg, ip, porta):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.connect((ip, porta))
        con.send(msg.encode())
        con.close()

    def set_key(self, key):
        self.key = key
        return self.key
    
    def send_to_ca(self, msg, ca_ip, ca_porta, destinatario_id, ca):
        chave_publica_destinatario = ca.consultar_chave_publica(destinatario_id)
        if chave_publica_destinatario is None:
            print(f"Erro: Chave pública do destinatário não encontrada.")
            return

        msg_criptografada = rsa.encrypt(msg.encode(), chave_publica_destinatario)

        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.connect((ca_ip, ca_porta))
        con.send(msg_criptografada)
        con.close()

