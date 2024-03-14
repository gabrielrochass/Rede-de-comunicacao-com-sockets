# cada pc deve ser capaz de se comunicar com seus vizinhos e com a CA (Certificate Authority)
# se comunica com PC3, PC5 e CA
import socket
from utils import send_message_to_pc

# hosts de cada pc e da CA para se comunicar
PC2_HOST = 'pc2'
PC6_HOST = 'pc6'
CA_HOST = 'ca'
PORT_PC1 = 1000