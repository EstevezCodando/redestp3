# 🛠 O Que é e Como Funciona um Raw Socket?

Um **raw socket** permite acesso direto aos pacotes de rede, possibilitando a manipulação de protocolos de baixo nível como **ICMP, IP e TCP**. Diferente dos sockets convencionais, ele não processa automaticamente cabeçalhos, exigindo que o desenvolvedor construa e interprete manualmente os pacotes.

## 🔍 Funcionamento
- Utilizado para **análise de rede, segurança e diagnóstico**.
- Permite **envio e recepção** de pacotes sem a camada de transporte (TCP/UDP).
- Necessita **privilégios administrativos** para ser executado.

## 📌 Exemplo Prático: Ping Personalizado com ICMP
O código abaixo cria um **ping personalizado**, enviando pacotes **ICMP Echo Request** e capturando as respostas:

```python
import socket
import struct
import time

def calcular_checksum(dados):
    soma = sum(dados[i] + (dados[i+1] << 8) for i in range(0, len(dados), 2))
    soma = (soma & 0xFFFF) + (soma >> 16)
    return ~soma & 0xFFFF

def criar_pacote_icmp():
    tipo = 8  # Echo Request
    codigo = 0
    identificador = 1
    sequencia = 1
    payload = b'PingTeste'
    cabecalho = struct.pack("!BBHHH", tipo, codigo, 0, identificador, sequencia)
    checksum = calcular_checksum(cabecalho + payload)
    cabecalho = struct.pack("!BBHHH", tipo, codigo, checksum, identificador, sequencia)
    return cabecalho + payload

def ping(destino):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.sendto(criar_pacote_icmp(), (destino, 0))
    inicio = time.time()
    sock.recv(1024)
    print(f"Resposta de {destino} em {round((time.time() - inicio) * 1000, 2)}ms")

ping("8.8.8.8")  # Teste clasico com o Google DNS
```

## ⚠️ Considerações
- Requer **execução como root** (`sudo python3 script.py`).
- Manipula diretamente pacotes, sem tratamento do sistema operacional.
- Usado para **ferramentas de monitoramento e segurança**.

