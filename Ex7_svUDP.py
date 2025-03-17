import socket

class ServidorUDP:
    """ Classe responsável por iniciar um servidor UDP e processar mensagens dos clientes. """

    def __init__(self, endereco: str, porta: int):
        self.endereco = endereco
        self.porta = porta
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_servidor.bind((self.endereco, self.porta))

    def iniciar(self):
        """ Inicia o servidor UDP e aguarda mensagens dos clientes. """
        print(f"Servidor UDP iniciado em {self.endereco}:{self.porta}")

        try:
            while True:
                mensagem, endereco_cliente = self.socket_servidor.recvfrom(4096)
                mensagem_decodificada = mensagem.decode().strip()
                print(f"[{endereco_cliente[0]}:{endereco_cliente[1]}] {mensagem_decodificada}")

                resposta = "Servidor UDP: Mensagem recebida com sucesso!"
                self.socket_servidor.sendto(resposta.encode(), endereco_cliente)

        except KeyboardInterrupt:
            print("\nServidor UDP encerrado.")
        finally:
            self.encerrar()

    def encerrar(self):
        """ Fecha o socket do servidor. """
        self.socket_servidor.close()
        print("Servidor finalizado.")

if __name__ == "__main__":
    servidor = ServidorUDP("0.0.0.0", 6789)  # Aceita conexões em qualquer IP na porta 6789
    servidor.iniciar()
