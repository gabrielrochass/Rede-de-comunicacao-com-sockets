# pra que serve a autoridade certificadora?
# importando diff hellman
import cryptography.hazmat.primitives.asymmetric.x25519 as x25519

# criando um dicionario para armazenar os endereços e portas de comunicação entre cliente e servidor.
info = {
    'pc1': ('100.000.0.0', 1000),
    'pc2': ('200.000.0.0', 2000),
    'pc3': ('300.000.0.0', 3000),
    'pc4': ('400.000.0.0', 4000),
    'pc5': ('500.000.0.0', 5000),
    'pc6': ('600.000.0.0', 6000),
    'ca': ('700.000.0.0', 7000)
}

print(info['pc1'][0]) # endereco ip do pc1
print(info['pc1'][1]) # porta de comunicacao (socket) do pc1