import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Criando a conexão
print('Socket Criado com sucesso !')

host = 'localhost'
port = 5432

s.bind((host, port))
mesage = 'Servidor : Salve Cliente, Jóia?'

while 1:  #enquanto 1 for verdadeiro
    dados, end = s.recvfrom(4096)

    if dados: #se houver dados
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mesage.encode()), end)    
    