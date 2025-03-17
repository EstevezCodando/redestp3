import socket

class ClienteUDP:
    """ Classe responsável por enviar mensagens ao servidor UDP e receber respostas. """

    def __init__(self, endereco_servidor: str, porta: int):
        self.endereco_servidor = endereco_servidor
        self.porta = porta
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def iniciar(self):
        """ Inicia a interação com o servidor UDP. """
        try:
            while True:
                mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ").strip()
                if not mensagem:
                    continue
                
                self.socket_cliente.sendto(mensagem.encode(), (self.endereco_servidor, self.porta))

                if mensagem.lower() == "sair":
                    break

                resposta, _ = self.socket_cliente.recvfrom(4096)
                print(f"Servidor: {resposta.decode()}")

        except KeyboardInterrupt:
            print("\nCliente encerrado.")
        finally:
            self.encerrar()

    def encerrar(self):
        """ Fecha o socket do cliente. """
        self.socket_cliente.close()
        print("Conexão finalizada.")

if __name__ == "__main__":
    cliente = ClienteUDP("127.0.0.1", 6789)  # Conectar ao servidor UDP local na porta 6789
    cliente.iniciar()
