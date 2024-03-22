class Roteador:
    def __init__(self, hosts, adjacentes, certification):
        self.hosts = hosts
        self.adjacentes = adjacentes
        self.certification = certification
        self.path = {
            1: [hosts[0],hosts[1],hosts[1],hosts[1],hosts[5],hosts[5]], 
            2: [hosts[0],hosts[1],hosts[2],hosts[2],hosts[2],hosts[0]],
            3: [hosts[1],hosts[1],hosts[2],hosts[3],hosts[3],hosts[3]],
            4: [hosts[2],hosts[2],hosts[2],hosts[3],hosts[4],hosts[4]],
            5: [hosts[5],hosts[3],hosts[3],hosts[3],hosts[4],hosts[5]],
            6: [hosts[0],hosts[0],hosts[4],hosts[4],hosts[4],hosts[5]]
        }

    def rota(self, origem, destino, mensagem):
        if destino in self.adjacentes[origem.nome]:
            origem.send_encrypted(mensagem, destino.ip, destino.porta, destino.id, self.certification)
            return
        else:
            pc_atual = self.path[origem.id]
            i = destino.id - 1
            origem.send_encrypted(mensagem, pc_atual[i].ip, pc_atual[i].porta, destino.id, self.certification)
            self.rota(pc_atual[i], destino, mensagem)           