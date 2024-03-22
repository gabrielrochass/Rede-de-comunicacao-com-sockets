# pra que serve a autoridade certificadora?
# importando diff hellman
# import cryptography.hazmat.primitives.asymmetric.x25519 as x25519
import rsa
import socket
class AutoridadeCertificadora:
    def __init__(self):
        self.chaves_publicas = {}

    def registrar(self, id):
        chave_publica, chave_privada = rsa.newkeys(512)
        self.chaves_publicas[id] = chave_publica
        return chave_privada

    def consultar_chave_publica(self, id):
        return self.chaves_publicas.get(id)
    
    def listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('127.0.0.7', 7000))
        self.socket.listen()

        while True:
            con, _ = self.socket.accept()
            msg = con.recv(2048)
            print(f'CA recebeu mensagem criptografada: {msg.hex()}')
            # Aqui você deve descriptografar a mensagem e encaminhá-la para o destinatário
            con.close()

# # Exemplo de uso da classe AutoridadeCertificadora
# ac = AutoridadeCertificadora()
# id = ac.id
# chave_privada = ac.registrar(id)
# chave_publica = ac.consultar_chave_publica(id)
# print(f"Chave privada: {chave_privada}")
# print(f"Chave pública: {chave_publica}")

pubkey, privkey = rsa.newkeys(512)

# Dados a serem criptografados
data = b'hello world'

# Criptografa os dados com a chave pública
ciphertext = rsa.encrypt(data, chave_publica)
print(f'Ciphertext: {ciphertext.hex()}')

# Descriptografa os dados com a chave privada
plaintext = rsa.decrypt(ciphertext, chave_privada)

print(f'Plaintext: {plaintext.decode("utf-8")}')