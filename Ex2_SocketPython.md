# 📡 O Pacote `socket` em Python

O pacote `socket` em Python fornece suporte para comunicação em rede, permitindo a criação e manipulação de **sockets**, que são interfaces para troca de dados entre processos locais ou remotos.

## 🛠 Criando um Socket

A criação de um socket em Python segue a estrutura:

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Onde:
- `AF_INET` → Define a família de endereços (IPv4). Para IPv6, utiliza-se `AF_INET6`.
- `SOCK_STREAM` → Define o tipo de socket para conexões TCP. Para UDP, utiliza-se `SOCK_DGRAM`.

## 🔄 Funcionamento

### **No Servidor**
1. **Criar o socket:** `socket.socket()`
2. **Associar a um endereço e porta:** `bind()`
3. **Aguardar conexões:** `listen()`
4. **Aceitar conexões:** `accept()`
5. **Trocar dados:** `send()` e `recv()`
6. **Encerrar:** `close()`

### **No Cliente**
1. **Criar o socket:** `socket.socket()`
2. **Conectar ao servidor:** `connect()`
3. **Trocar dados:** `send()` e `recv()`
4. **Encerrar:** `close()`

## 🔹 Métodos Principais
- **`bind((host, porta))`** → Associa o socket a um endereço IP e porta.
- **`listen(qtd)`** → Coloca o socket em modo de escuta.
- **`accept()`** → Aceita conexões de clientes (somente para servidores).
- **`connect((host, porta))`** → Estabelece conexão com um servidor (somente para clientes).
- **`send(dados)` / `sendall(dados)`** → Envia dados pelo socket.
- **`recv(tamanho)`** → Recebe dados do socket.
- **`close()`** → Fecha a conexão.

## 🌐 Aplicações
Os sockets são usados em **servidores web**, **comunicação entre processos**, **transferência de arquivos**, **jogos multiplayer** e **monitoramento de rede**.