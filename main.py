# importando as bibliotecas e classes
import threading
from pc import PC
from ca import AutoridadeCertificadora
from mecanism import Roteador


def broadcast(origin, pcs):
    for pc in pcs:
        if (pc != origin): 
            router.rota(origin, pc, 'BROADCAST')
            if (pc.message == 'BROADCAST') :
                router.rota(pc, origin, f'RECEBI de {pc.nome}')


# cria a autoridade certificadora
ac = AutoridadeCertificadora()


# cria os pcs
pc1 = PC(nome='PC1', ip='127.0.0.1', porta=1000, id=1, message= 'nada')
pc2 = PC(nome='PC2', ip='127.0.0.2', porta=2000, id=2, message= 'nada')
pc3 = PC(nome='PC3', ip='127.0.0.3', porta=3000, id=3, message= 'nada')
pc4 = PC(nome='PC4', ip='127.0.0.4', porta=4000, id=4, message= 'nada')
pc5 = PC(nome='PC5', ip='127.0.0.5', porta=5000, id=5, message= 'nada')
pc6 = PC(nome='PC6', ip='127.0.0.6', porta=6000, id=6, message= 'nada')


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


for pc in pcs:
    threading.Thread(target=pc.listen_encrypted).start()


router.rota(pc1, pc2, 'Hello from PC1 to PC2')
router.rota(pc1, pc3, 'Hello from PC1 to PC3')
router.rota(pc1, pc4, 'Hello from PC1 to PC4')
router.rota(pc1, pc5, 'Hello from PC1 to PC5')
router.rota(pc1, pc6, 'Hello from PC1 to PC6')

broadcast(pc1, pcs)

#Repetindo o processo agora com todos os PCs
for pc_origem in pcs:
    for pc_destino in pcs:
        if pc_destino != pc_origem:
            router.rota(pc_origem, pc_destino, f'Hello from {pc_origem.nome} to {pc_destino.nome}')
    broadcast(pc_origem, pcs)



