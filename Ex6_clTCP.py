import socket

class ClienteTCP:
    """ Classe responsável por estabelecer conexão com o servidor TCP e enviar mensagens. """

    def __init__(self, endereco_servidor: str, porta: int):
        self.endereco_servidor = endereco_servidor
        self.porta = porta
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        """ Conecta ao servidor TCP e inicia a interação. """
        try:
            self.socket_cliente.connect((self.endereco_servidor, self.porta))
            print(f"Conectado ao servidor {self.endereco_servidor}:{self.porta}")

            # Recebe a mensagem de boas-vindas do servidor
            mensagem_boas_vindas = self.socket_cliente.recv(1024).decode()
            print(f"Servidor: {mensagem_boas_vindas}")

            self.interagir()

        except socket.error as erro:
            print(f"Erro de conexão: {erro}")
        finally:
            self.encerrar()

    def interagir(self):
        """ Loop de interação com o servidor, enviando mensagens e recebendo respostas. """
        try:
            while True:
                mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ").strip()
                if not mensagem:
                    continue
                
                self.socket_cliente.sendall(mensagem.encode())

                if mensagem.lower() == "sair":
                    break

                resposta = self.socket_cliente.recv(1024).decode()
                if not resposta:
                    print("Conexão com o servidor foi encerrada.")
                    break
                
                print(f"Servidor: {resposta}")

        except (socket.error, KeyboardInterrupt):
            print("\nConexão com o servidor encerrada inesperadamente.")

    def encerrar(self):
        """ Fecha a conexão com o servidor. """
        self.socket_cliente.close()
        print("Conexão encerrada.")

if __name__ == "__main__":
    cliente = ClienteTCP("127.0.0.1", 9999)  # Conectar ao servidor local na porta 9999
    cliente.conectar()
