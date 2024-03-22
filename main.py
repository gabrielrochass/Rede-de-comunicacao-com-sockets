# importa as classes
# cria os pcs
# usa a politica de roteamento
# cria a ca
import threading
from pc import PC
from ca import AutoridadeCertificadora
ac = AutoridadeCertificadora()

pc1 = PC(nome='PC1', ip='127.0.0.1', porta=1000, id=1)
pc2 = PC(nome='PC2', ip='127.0.0.2', porta=2000, id=2)
pc3 = PC(nome='PC3', ip='127.0.0.3', porta=3000, id=3)
pc4 = PC(nome='PC4', ip='127.0.0.4', porta=4000, id=4)
pc5 = PC(nome='PC5', ip='127.0.0.5', porta=5000, id=5)
pc6 = PC(nome='PC6', ip='127.0.0.6', porta=6000, id=6)

vizinhos = {
    'PC1': [pc2, pc6],
    'PC2': [pc1, pc3],
    'PC3': [pc2, pc4],
    'PC4': [pc3, pc5],
    'PC5': [pc4, pc6],
    'PC6': [pc5, pc1]
}

# gerar as chaves publicas e privadas com ca
pc1.set_key(ac.registrar(pc1.id))
pc2.set_key(ac.registrar(pc2.id))
pc3.set_key(ac.registrar(pc3.id))
pc4.set_key(ac.registrar(pc4.id))
pc5.set_key(ac.registrar(pc5.id))
pc6.set_key(ac.registrar(pc6.id))

def roteamento(pc_origem, pc_destino, msg):
    if pc_destino in vizinhos[pc_origem.nome]: 
        pc_origem.send_encrypted(msg, pc_destino.ip, pc_destino.porta, pc_destino.id, ac)
        return
    else:
        oposto = (pc_origem.id + 3) % 6
        # printar caminho
        if oposto == 0:
            oposto = 6
        if pc_origem.id > oposto:
            # print(f'{pc_origem.nome} -> {vizinhos[pc_origem.nome][1].nome} -> {pc_destino.nome}')
            roteamento(vizinhos[pc_origem.nome][1], pc_destino , msg) 
        else:
            # print(f'{pc_origem.nome} -> {vizinhos[pc_origem.nome][0].nome} -> {pc_destino.nome}')
            roteamento(vizinhos[pc_origem.nome][0], pc_destino, msg)
        

pcs = [pc1, pc2, pc3, pc4, pc5, pc6]
for pc in pcs:
    threading.Thread(target=pc.listen_encrypted).start()

# pc1.send_encrypted('Hello from PC1', pc2.ip, pc2.porta, pc2.id, ac)
roteamento(pc1, pc4, 'Hello from PC1 to PC4')
