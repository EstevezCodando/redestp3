import socket
import threading
import os

class ServidorHTTP:
    """ Classe responsável por iniciar um servidor HTTP simples. """

    def __init__(self, host="127.0.0.1", porta=8080, arquivo_html="index.html"):
        self.host = host
        self.porta = porta
        self.arquivo_html = arquivo_html
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reuso imediato da porta

    def iniciar(self):
        """ Inicia o servidor e aguarda conexões. """
        try:
            self.socket_servidor.bind((self.host, self.porta))
            self.socket_servidor.listen(5)  # Suporta até 5 conexões na fila
            print(f"Servidor HTTP rodando em http://{self.host}:{self.porta}")

            while True:
                conexao, endereco = self.socket_servidor.accept()
                thread_cliente = threading.Thread(target=self.tratar_requisicao, args=(conexao,))
                thread_cliente.start()

        except KeyboardInterrupt:
            print("\nServidor HTTP encerrado.")
        finally:
            self.encerrar()

    def tratar_requisicao(self, conexao: socket.socket):
        """ Processa a requisição HTTP do cliente. """
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
        self.socket_servidor.close()
        print("Servidor finalizado.")

if __name__ == "__main__":
    servidor = ServidorHTTP()
    servidor.iniciar()
