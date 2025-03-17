import socket

class ClienteHTTP:
    """ Cliente HTTP simples que se conecta a um servidor e faz uma requisição GET. """

    def __init__(self, host: str, porta: int):
        self.host = host
        self.porta = porta
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        """ Conecta ao servidor HTTP. """
        try:
            self.socket_cliente.connect((self.host, self.porta))
            print(f"Conectado a {self.host} na porta {self.porta}")

            self.enviar_requisicao()
        except socket.error as erro:
            print(f"Erro de conexão: {erro}")
        finally:
            self.encerrar()

    def enviar_requisicao(self):
        """ Envia uma requisição GET ao servidor e processa a resposta. """
        try:
            requisicao = f"GET / HTTP/1.1\r\nHost: {self.host}\r\nConnection: close\r\n\r\n"
            self.socket_cliente.sendall(requisicao.encode('utf-8'))
            print(f"Requisição enviada:\n{requisicao}")

            self.receber_resposta()
        except socket.error as erro:
            print(f"Erro ao enviar requisição: {erro}")

    def receber_resposta(self):
        """ Recebe e exibe a resposta do servidor HTTP. """
        resposta_completa = b""
        
        # Loop para garantir que toda a resposta seja recebida
        while True:
            fragmento = self.socket_cliente.recv(4096)
            if not fragmento:
                break
            resposta_completa += fragmento

        resposta_decodificada = resposta_completa.decode('utf-8')

        # Exibir código de status HTTP separadamente
        linhas = resposta_decodificada.split("\r\n")
        print(f"\n[+] Código de Status: {linhas[0]}")
        print("[+] Resposta do Servidor:")
        print(resposta_decodificada)

    def encerrar(self):
        """ Fecha o socket do cliente. """
        self.socket_cliente.close()
        print("Conexão encerrada.")

if __name__ == "__main__":
    cliente = ClienteHTTP("127.0.0.1", 8080)
    cliente.conectar()
