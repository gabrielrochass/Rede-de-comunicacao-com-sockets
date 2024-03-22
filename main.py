# importando as bibliotecas e classes
import threading
from pc import PC
from ca import AutoridadeCertificadora
from mecanism import Roteador

# cria a autoridade certificadora
ac = AutoridadeCertificadora()

# cria os pcs
pc1 = PC(nome='PC1', ip='127.0.0.1', porta=1000, id=1)
pc2 = PC(nome='PC2', ip='127.0.0.2', porta=2000, id=2)
pc3 = PC(nome='PC3', ip='127.0.0.3', porta=3000, id=3)
pc4 = PC(nome='PC4', ip='127.0.0.4', porta=4000, id=4)
pc5 = PC(nome='PC5', ip='127.0.0.5', porta=5000, id=5)
pc6 = PC(nome='PC6', ip='127.0.0.6', porta=6000, id=6)

pcs = [pc1, pc2, pc3, pc4, pc5, pc6]

vizinhos = {
    'PC1': [pc2, pc6],
    'PC2': [pc1, pc3],
    'PC3': [pc2, pc4],
    'PC4': [pc3, pc5],
    'PC5': [pc4, pc6],
    'PC6': [pc5, pc1]
}

router = Roteador(pcs,vizinhos,ac)

# gerar as chaves publicas e privadas com ca
for j in pcs:
    j.set_key(ac.registrar(j.id))

'''def roteamento(pc_origem, pc_destino, msg):
    if pc_destino in vizinhos[pc_origem.nome]: 
        pc_origem.send_encrypted(msg, pc_destino.ip, pc_destino.porta, pc_destino.id, ac)
        return
    else:
        path = {
            1: [pc1,pc2,pc2,pc2,pc6,pc6], 
            2: [pc1,pc2,pc3,pc3,pc3,pc1],
            3: [pc2,pc2,pc3,pc4,pc4,pc4],
            4: [pc3,pc3,pc3,pc4,pc5,pc5],
            5: [pc6,pc4,pc4,pc4,pc5,pc6],
            6: [pc1,pc1,pc5,pc5,pc5,pc6]
        }
        pc_atual = path[pc_origem.id]
        i = pc_destino.id - 1
        pc_origem.send_encrypted(msg, pc_atual[i].ip, pc_atual[i].porta, pc_destino.id, ac)
        roteamento(pc_atual[i], pc_destino, msg)'''
       

for pc in pcs:
    threading.Thread(target=pc.listen_encrypted).start()

router.rota(pc1, pc4, 'Hello from PC1 to PC4')
router.rota(pc1, pc6, 'Hello from PC1 to PC6')
router.rota(pc2, pc1, 'Hello from PC2 to PC1')
router.rota(pc3, pc5, 'Hello from PC3 to PC5')
router.rota(pc4, pc1, 'Hello from PC4 to PC1')



