# classe de pc pra impotar main
import socket
import rsa #dar um pip install rsa caso não previamente instalado

class PC:
    def __init__(self, nome, ip, porta, id):
        self.nome = nome
        self.ip = ip
        self.porta = porta
        self.id = id

    def set_key(self, key):
        self.key = key
        return self.key
    
    def send(self, msg, ip, porta):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.connect((ip, porta))
        con.send(msg.encode())
        con.close()
    
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
            try:
                decrypted_msg = rsa.decrypt(msg, self.key)
                print(f'{self.nome} recebeu: {decrypted_msg.decode()}')
            except Exception as e:
                print(f'{self.nome} recebeu um erro ao descriptografar mensagem: {e}')   
            finally:
                con.close()

    def encriptar(self, msg, chave_publica):
        return rsa.encrypt(msg.encode(), chave_publica)
        
