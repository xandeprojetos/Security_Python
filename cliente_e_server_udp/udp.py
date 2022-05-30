import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Protocolo de datagrama
print('Cliente socket criado com sucesso !')

host = 'localhost'
porta = 5433
mesage = 'Olá servidor, tranquilidade?'

try: 
    print('Cliente: ' + mesage)
    s.sendto(mesage.encode(), (host, 5432)) #empacotando

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)

finally:
    print('Cliente: Fechando a conexão')
    s.close() 
 
