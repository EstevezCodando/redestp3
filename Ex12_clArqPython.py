import socket
import struct
import os

HOST = 'localhost'
PORT = 9999
BUFFER_SIZE = 1024
DIRETORIO_DOWNLOADS = "client_downloads"

os.makedirs(DIRETORIO_DOWNLOADS, exist_ok=True)

def receber_arquivo(sock: socket.socket, nome_arquivo):
    """Recebe um arquivo do servidor e salva no diretório do cliente."""
    tamanho_arquivo = struct.unpack("<Q", sock.recv(struct.calcsize("<Q")))[0]
    if tamanho_arquivo == 0:
        print("[-] Servidor: Arquivo não encontrado.")
        return False

    caminho_arquivo = os.path.join(DIRETORIO_DOWNLOADS, nome_arquivo)
    with open(caminho_arquivo, "wb") as arquivo:
        recebido = 0
        while recebido < tamanho_arquivo:
            fragmento = sock.recv(min(BUFFER_SIZE, tamanho_arquivo - recebido))
            if not fragmento:
                break
            arquivo.write(fragmento)
            recebido += len(fragmento)

    print(f"[+] Arquivo baixado: {caminho_arquivo} ({tamanho_arquivo} bytes)")
    return True

def executar_cliente():
    """Executa o cliente e permite comandos do usuário."""
    with socket.create_connection((HOST, PORT)) as sock:
        print(f"[+] Conectado ao servidor {HOST}:{PORT}")

        while True:
            comando = input("\nDigite um comando (LIST, UPLOAD <arquivo>, DOWNLOAD <arquivo>, QUIT): ").strip()

            if comando.upper() == "LIST":
                sock.sendall(b"LIST")
                print(sock.recv(4096).decode())

            elif comando.upper().startswith("UPLOAD"):
                _, nome_arquivo = comando.split(maxsplit=1)
                if os.path.exists(nome_arquivo):
                    sock.sendall(b"UPLOAD")
                    sock.sendall(nome_arquivo.encode())
                    with open(nome_arquivo, "rb") as arquivo:
                        sock.sendfile(arquivo)
                else:
                    print("[-] Arquivo não encontrado.")

            elif comando.upper().startswith("DOWNLOAD"):
                _, nome_arquivo = comando.split(maxsplit=1)
                sock.sendall(b"DOWNLOAD")
                sock.sendall(nome_arquivo.encode())
                receber_arquivo(sock, nome_arquivo)

            elif comando.upper() == "QUIT":
                sock.sendall(b"QUIT")
                break

if __name__ == "__main__":
    executar_cliente()
