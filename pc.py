# classe de pc pra impotar main
import socket
import rsa #dar um pip install rsa caso não previamente instalado
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class PC:
    def __init__(self, nome, ip, porta, id):
        self.nome = nome
        self.ip = ip
        self.porta = porta
        #self.porta_broadcast = broadcast
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
        con.connect((ip, porta))
        
        chave_simetrica = get_random_bytes(16)
        chave_publica_dest = ca.consultar_chave_publica(id)
        chave_simetrica_cifrada = rsa.encrypt(chave_simetrica, chave_publica_dest)
        cipher = AES.new(chave_simetrica, AES.MODE_EAX)
        
        # Criptografar a mensagem
        ciphertext, tag = cipher.encrypt_and_digest(msg.encode())

        # Enviar a chave simétrica cifrada, o nonce, o tag e o texto cifrado
        con.send(chave_simetrica_cifrada)
        con.send(cipher.nonce)
        con.send(tag)
        con.send(ciphertext)

        con.close()

    def listen_encrypted(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.porta))
        self.socket.listen()

        while True:
            con, _ = self.socket.accept()
            chave_simetrica_cifrada = con.recv(2048)
            nonce = con.recv(16)
            tag = con.recv(16)
            ciphertext = con.recv(2048)

            # Decifrar a mensagem
            try:
                # Decifrar a chave simétrica
                chave_simetrica = rsa.decrypt(chave_simetrica_cifrada, self.key)

                # Criar o objeto de cifra simétrica
                cipher = AES.new(chave_simetrica, AES.MODE_EAX, nonce=nonce)

                plaintext = cipher.decrypt_and_verify(ciphertext, tag)
                print(f'{self.nome} recebeu: {plaintext.decode()}')
            except Exception as e:
                print(f'{self.nome} recebeu um erro ao descriptografar mensagem: {e}')   
            finally:
                con.close()


    
    def broadcast(self, msg, pcs, ca):
        for pc in pcs:
            self.send_encrypted(self, msg, pc.ip, pc.porta_broadcast, pc.id, ca)

    def listen_broadcast(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.porta_broadcast))
        self.socket.listen()

        while True:
            con, _ = self.socket.accept()
            msg = con.recv(2048)
            print(f'{self.nome} recebeu: {msg.decode()}')
            self.send('Recebi',)
            con.close()
        
        
