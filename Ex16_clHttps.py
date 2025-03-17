import socket
import ssl

class ClienteHTTPSSeguro:
    """ Cliente HTTPS simples que se conecta a um servidor e faz uma requisição GET segura. """

    def __init__(self, host: str, porta: int):
        self.host = host
        self.porta = porta

        # Criando o socket TCP normal
        self.socket_cliente = socket.create_connection((self.host, self.porta))

        # Criando um contexto SSL para conexão segura
        contexto_ssl = ssl.create_default_context()
        contexto_ssl.check_hostname = False  # Desativa verificação do hostname
        contexto_ssl.verify_mode = ssl.CERT_NONE  # Desativa verificação do certificado (autoassinado)

        # Envelopando o socket com SSL
        self.socket_ssl = contexto_ssl.wrap_socket(self.socket_cliente, server_hostname=self.host)

    def conectar(self):
        """ Conecta ao servidor HTTPS. """
        try:
            print(f"🔒 Conectado a {self.host} na porta {self.porta} via HTTPS")

            self.enviar_requisicao()
        except socket.error as erro:
            print(f"❌ Erro de conexão: {erro}")
        finally:
            self.encerrar()

    def enviar_requisicao(self):
        """ Envia uma requisição GET ao servidor e processa a resposta. """
        try:
            requisicao = f"GET / HTTP/1.1\r\nHost: {self.host}\r\nConnection: close\r\n\r\n"
            self.socket_ssl.sendall(requisicao.encode('utf-8'))
            print(f"📡 Requisição enviada:\n{requisicao}")

            self.receber_resposta()
        except socket.error as erro:
            print(f"❌ Erro ao enviar requisição: {erro}")

    def receber_resposta(self):
        """ Recebe e exibe a resposta do servidor HTTPS. """
        resposta_completa = b""
        
        # Loop para garantir que toda a resposta seja recebida
        while True:
            fragmento = self.socket_ssl.recv(4096)
            if not fragmento:
                break
            resposta_completa += fragmento

        resposta_decodificada = resposta_completa.decode('utf-8')

        # Exibir código de status HTTP separadamente
        linhas = resposta_decodificada.split("\r\n")
        print(f"\n🔹 **Código de Status:** {linhas[0]}")
        print("🔹 **Resposta do Servidor:**")
        print(resposta_decodificada)

    def encerrar(self):
        """ Fecha o socket seguro. """
        self.socket_ssl.close()
        print("🔒 Conexão segura encerrada.")

if __name__ == "__main__":
    cliente = ClienteHTTPSSeguro("127.0.0.1", 8443)
    cliente.conectar()
