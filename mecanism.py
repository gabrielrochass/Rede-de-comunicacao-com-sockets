class Roteador:
    def __init__(self, hosts, adjacentes, certificator):
        self.hosts = hosts
        self.adjacentes = adjacentes
        self.certificator = certificator
        self.path = {
            1: [hosts[0],hosts[1],hosts[1],hosts[1],hosts[5],hosts[5]], # [pc1,pc2,pc2,pc2,pc6,pc6]
            2: [hosts[0],hosts[1],hosts[2],hosts[2],hosts[2],hosts[0]], # [pc1,pc2,pc3,pc3,pc3,pc1]
            3: [hosts[1],hosts[1],hosts[2],hosts[3],hosts[3],hosts[3]], # [pc2,pc2,pc3,pc4,pc4,pc4]
            4: [hosts[2],hosts[2],hosts[2],hosts[3],hosts[4],hosts[4]], # [pc3,pc3,pc3,pc4,pc5,pc5]
            5: [hosts[5],hosts[3],hosts[3],hosts[3],hosts[4],hosts[5]], # [pc6,pc4,pc4,pc4,pc5,pc6]
            6: [hosts[0],hosts[0],hosts[4],hosts[4],hosts[4],hosts[5]]  # [pc1,pc1,pc5,pc5,pc5,pc6]
        }


    def rota(self, origem, destino, mensagem):
        if destino in self.adjacentes[origem.nome]:
            origem.send_encrypted(mensagem, destino.ip, destino.porta, destino.id, self.certificator)
            return
        else:
            pc_atual = self.path[origem.id]
            i = destino.id - 1
            origem.send_encrypted(mensagem, pc_atual[i].ip, pc_atual[i].porta, destino.id, self.certificator)
            self.rota(pc_atual[i], destino, mensagem)          


