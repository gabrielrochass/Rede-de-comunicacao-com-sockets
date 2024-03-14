# cada pc deve ser capaz de se comunicar com seus vizinhos e com a CA (Certificate Authority)
# se comunica com PC2, PC6 e CA

import socket
from utils import send_message_to_pc
from utils import receive_message_from_pc

# portas vizinhas
neighbors = [2000, 6000]

# hosts de cada pc e da CA para se comunicar
PC2_HOST = 'pc2'
PC6_HOST = 'pc6'
CA_HOST = 'ca'
PORT_PC1 = 1000

    
# teste
receive_message_from_pc(neighbors)
