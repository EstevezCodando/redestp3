import socket
import threading

def escanear_porta(ip, porta):
    """Tenta conectar à porta especificada no IP fornecido."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Define um timeout para a tentativa de conexão
            resultado = s.connect_ex((ip, porta))
            if resultado == 0:
                print(f"[+] Porta {porta} ABERTA")
    except Exception as e:
        print(f"Erro ao escanear a porta {porta}: {e}")

def escanear_rede(ip, porta_inicial, porta_final):
    """Executa o escaneamento de um intervalo de portas em um IP."""
    print(f"Iniciando escaneamento em {ip} nas portas {porta_inicial}-{porta_final}")

    threads = []
    for porta in range(porta_inicial, porta_final + 1):
        thread = threading.Thread(target=escanear_porta, args=(ip, porta))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Escaneamento concluído.")

if __name__ == "__main__":
    ip_alvo = input("Digite o endereço IP do alvo: ")
    porta_inicial = int(input("Digite a porta inicial: "))
    porta_final = int(input("Digite a porta final: "))

    escanear_rede(ip_alvo, porta_inicial, porta_final)
