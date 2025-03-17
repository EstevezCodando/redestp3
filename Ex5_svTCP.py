import socket
import threading

class ServidorTCP:
    """ Classe responsável por iniciar um servidor TCP e gerenciar múltiplas conexões. """

    def __init__(self, endereco: str, porta: int):
        self.endereco = endereco
        self.porta = porta
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar(self):
        """ Inicia o servidor e aguarda conexões de clientes. """
        try:
            self.socket_servidor.bind((self.endereco, self.porta))
            self.socket_servidor.listen(5)  # Aceita até 5 conexões simultâneas na fila
            print(f"Servidor TCP iniciado em {self.endereco}:{self.porta}")

            while True:
                conexao, endereco_cliente = self.socket_servidor.accept()
                print(f"[+] Conexão aceita de: {endereco_cliente[0]}:{endereco_cliente[1]}")

                thread_cliente = threading.Thread(target=self.tratar_cliente, args=(conexao,))
                thread_cliente.start()

        except KeyboardInterrupt:
            print("\nServidor encerrado.")
        finally:
            self.encerrar()

    def tratar_cliente(self, conexao: socket.socket):
        """ Manipula a comunicação com um cliente TCP. """
        try:
            conexao.send("Conectado ao servidor TCP!\n".encode())

            while True:
                mensagem = conexao.recv(1024).decode()
                if not mensagem or mensagem.lower() == "sair":
                    break
                print(f"Mensagem recebida: {mensagem}")
                conexao.send("ACK".encode())

        except ConnectionResetError:
            print("Cliente desconectado inesperadamente.")
        finally:
            conexao.close()

    def encerrar(self):
        """ Fecha o socket do servidor. """
        self.socket_servidor.close()
        print("Servidor finalizado.")

if __name__ == "__main__":
    servidor = ServidorTCP("0.0.0.0", 9999)  # Aceita conexões em qualquer IP na porta 9999
    servidor.iniciar()
