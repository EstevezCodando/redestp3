import socket
import ssl
import threading
import os
# primeiro tem que criar um certificado autoassinado, executando o comando abaixo no terminal
# openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

class ServidorHTTPSSeguro:
    """ Classe responsável por iniciar um servidor HTTPS usando TLS. """

    def __init__(self, host="127.0.0.1", porta=8443, arquivo_html="index.html", cert="cert.pem", key="key.pem"):
        self.host = host
        self.porta = porta
        self.arquivo_html = arquivo_html
        self.cert = cert
        self.key = key

        # Criando socket TCP
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Envelopando o socket com SSL/TLS
        self.socket_ssl = ssl.wrap_socket(
            self.socket_servidor,
            keyfile=self.key,
            certfile=self.cert,
            server_side=True
        )

    def iniciar(self):
        """ Inicia o servidor HTTPS e aguarda conexões. """
        try:
            self.socket_ssl.bind((self.host, self.porta))
            self.socket_ssl.listen(5)  # Suporta até 5 conexões na fila
            print(f"🔒 Servidor HTTPS rodando em https://{self.host}:{self.porta}")

            while True:
                conexao, endereco = self.socket_ssl.accept()
                thread_cliente = threading.Thread(target=self.tratar_requisicao, args=(conexao,))
                thread_cliente.start()

        except KeyboardInterrupt:
            print("\nServidor HTTPS encerrado.")
        finally:
            self.encerrar()

    def tratar_requisicao(self, conexao: ssl.SSLSocket):
        """ Processa a requisição HTTPS do cliente. """
        try:
            request = conexao.recv(1024).decode('utf-8')
            print(f"Requisição recebida:\n{request}")

            if "GET" not in request:
                resposta = "HTTP/1.1 405 Method Not Allowed\r\n\r\nMétodo não permitido"
            else:
                conteudo_html = self.carregar_html()
                resposta = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html\r\n"
                    f"Content-Length: {len(conteudo_html)}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                    f"{conteudo_html}"
                )

            conexao.sendall(resposta.encode('utf-8'))

        except Exception as erro:
            print(f"Erro ao processar requisição: {erro}")

        finally:
            conexao.close()

    def carregar_html(self) -> str:
        """ Lê o conteúdo do arquivo HTML para servir. """
        if os.path.exists(self.arquivo_html):
            with open(self.arquivo_html, "r", encoding="utf-8") as arquivo:
                return arquivo.read()
        else:
            return "<h1>Erro 404: Arquivo não encontrado</h1>"

    def encerrar(self):
        """ Encerra o servidor corretamente. """
        self.socket_ssl.close()
        print("Servidor HTTPS finalizado.")

if __name__ == "__main__":
    servidor = ServidorHTTPSSeguro()
    servidor.iniciar()
