import socket

# portas
allPorts = [1000, 2000, 3000, 4000, 5000, 6000]	

# envia mensagem para PC vizinho
def send_message_to_pc(host, port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(message.encode())
    data = s.recv(1024)

    print('Sent successfully:', data.decode())

# send_message_to_pc:
    # socket.socket: cria um objeto de soquete (método construtor)
    # socket.AF_INET: família de endereços que pode se comunicar, IPv4
    # socket.SOCK_STREAM: tipo de soquete, TCP
    # s.connect: conecta o soquete a um endereço
    # s.sendall: envia todos os dados da mensagem. 
    # Encode(): converte a string em bytes
    # s.recv: recebe dados do soquete. O argumento especifica o número máximo de bytes a serem recebidos, 1KB
    # Decode(): converte os bytes em string





# recebe mensagem do PC vizinho -> rever
def receive_message_from_pc(neighbors):
    while True:
        for port in neighbors:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('localhost', port))
            s.listen()
            acepted = s.accept()
            data = acepted.recv(1024)
            print('Received message:', data.decode())
            acepted.sendall(b'Message received successfully')
            acepted.close()
    