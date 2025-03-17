import socket
import struct
import os
import threading

# Configuração do Servidor
HOST = '0.0.0.0'
PORT = 9999
BUFFER_SIZE = 1024
DIRETORIO_ARQUIVOS = "server_files"

# Garante que o diretório de arquivos exista
os.makedirs(DIRETORIO_ARQUIVOS, exist_ok=True)

def enviar_tamanho_arquivo(sock: socket.socket, tamanho: int):
    """Envia o tamanho do arquivo para o cliente."""
    sock.sendall(struct.pack("<Q", tamanho))

def receber_tamanho_arquivo(sock: socket.socket):
    """Recebe o tamanho do arquivo do cliente."""
    tamanho_esperado = struct.calcsize("<Q")
    dados = sock.recv(tamanho_esperado)
    return struct.unpack("<Q", dados)[0] if dados else 0

def receber_arquivo(sock: socket.socket, nome_arquivo):
    """Recebe e salva um arquivo enviado pelo cliente."""
    tamanho_arquivo = receber_tamanho_arquivo(sock)
    if tamanho_arquivo == 0:
        print("[-] Erro: Arquivo não encontrado no cliente.")
        return False

    caminho_arquivo = os.path.join(DIRETORIO_ARQUIVOS, nome_arquivo)
    with open(caminho_arquivo, "wb") as arquivo:
        recebido = 0
        while recebido < tamanho_arquivo:
            fragmento = sock.recv(min(BUFFER_SIZE, tamanho_arquivo - recebido))
            if not fragmento:
                break
            arquivo.write(fragmento)
            recebido += len(fragmento)

    print(f"[+] Arquivo recebido: {caminho_arquivo} ({tamanho_arquivo} bytes)")
    return True

def enviar_arquivo(sock: socket.socket, nome_arquivo):
    """Envia um arquivo para o cliente."""
    caminho_arquivo = os.path.join(DIRETORIO_ARQUIVOS, nome_arquivo)
    if not os.path.exists(caminho_arquivo):
        sock.sendall(struct.pack("<Q", 0))  # Envia tamanho 0 para indicar erro
        print(f"[-] Arquivo não encontrado: {caminho_arquivo}")
        return False

    tamanho_arquivo = os.path.getsize(caminho_arquivo)
    enviar_tamanho_arquivo(sock, tamanho_arquivo)

    with open(caminho_arquivo, "rb") as arquivo:
        while (dados := arquivo.read(BUFFER_SIZE)):
            sock.sendall(dados)

    print(f"[+] Arquivo enviado: {caminho_arquivo} ({tamanho_arquivo} bytes)")
    return True

def tratar_cliente(sock, endereco):
    """Lida com um cliente e processa comandos."""
    print(f"[+] Conexão de {endereco[0]}:{endereco[1]}")

    try:
        while True:
            comando = sock.recv(BUFFER_SIZE).decode().strip()
            if not comando:
                break

            if comando.upper() == "LIST":
                arquivos = "\n".join(os.listdir(DIRETORIO_ARQUIVOS))
                sock.sendall(arquivos.encode() if arquivos else "Nenhum arquivo disponível.".encode())

            elif comando.upper().startswith("UPLOAD"):
                nome_arquivo = sock.recv(BUFFER_SIZE).decode().strip()
                receber_arquivo(sock, nome_arquivo)

            elif comando.upper().startswith("DOWNLOAD"):
                nome_arquivo = sock.recv(BUFFER_SIZE).decode().strip()
                enviar_arquivo(sock, nome_arquivo)

            elif comando.upper() == "QUIT":
                print(f"[-] Cliente {endereco} desconectado.")
                break

            else:
                sock.sendall("Comando inválido. Use LIST, UPLOAD, DOWNLOAD ou QUIT.\n".encode())

    except Exception as erro:
        print(f"[-] Erro ao tratar cliente {endereco}: {erro}")

    finally:
        sock.close()

def iniciar_servidor():
    """Inicia o servidor e aceita múltiplos clientes com threads."""
    with socket.create_server((HOST, PORT)) as servidor:
        print(f"[+] Servidor rodando em {HOST}:{PORT}")

        while True:
            conexao, endereco = servidor.accept()
            threading.Thread(target=tratar_cliente, args=(conexao, endereco), daemon=True).start()

if __name__ == "__main__":
    iniciar_servidor()
