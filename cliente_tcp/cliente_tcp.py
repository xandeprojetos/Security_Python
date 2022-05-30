import socket
import sys

def main():       #Definindo a função main
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as error: #Tratamento de erros
        print('A conexão falhou !')
        print('Error: {}'.format(error))
        sys.exit()      #esse comando irá fechar o programa

        
    print('Socket criado com sucesso !')    

    HostAlvo = input('Digite o host ou ip a ser conectado: ') #ip para ser conectado
    PortaAlvo = input('Digite a porta a ser conectada: ')     #porta para ser conectada

    try:
        s.connect((HostAlvo, int(PortaAlvo)))  #Segundo parametro não aceita string, então iremos transformar em um inteiro
        print('Cliente TCP conectado com sucesso no host: ' + HostAlvo + ' e na Porta: ' + PortaAlvo)

        s.shutdown(2)

    except socket.error as error:
        print('A conexão com o '+ HostAlvo +' e ' + PortaAlvo)
        print('Error: {}'. format(error))
        sys.exit()

if __name__ == "__main__":
    main()
