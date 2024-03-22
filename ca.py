import rsa

class AutoridadeCertificadora:
    def __init__(self):
        self.chaves_publicas = {}

    def registrar(self, id):
        chave_publica, chave_privada = rsa.newkeys(512)
        self.chaves_publicas[id] = chave_publica
        return chave_privada

    def consultar_chave_publica(self, id):
        return self.chaves_publicas.get(id)
