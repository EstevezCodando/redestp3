# 📡 Rede TP3 - Implementação de Sockets e Segurança em Python

Este repositório contém implementações relacionadas a **sockets, redes e segurança** utilizando a linguagem **Python**. 
Cada exercício aborda um aspecto fundamental da comunicação em rede, desde **sockets TCP/UDP**, **servidores HTTP**, até **segurança com SSL/TLS**.

---

## 📌 Exercícios e Implementações

### 📝 **1. O que são e como são usados os sockets?**
📄 [Ex1_Sockets.md](Ex1_Sockets.md)  
Explicação com minhas palavras de forma bem resumida sobre **o conceito de sockets**, seu funcionamento e como são utilizados para comunicação entre processos em redes.

---

### 📝 **2. O pacote `socket` em Python**
📄 [Ex2_SocketPython.md](Ex2_SocketPython.md)  
Descrição sobre o pacote `socket` do Python, abordando **a criação de sockets** e os principais **métodos disponíveis**.

---

### 📝 **3. O que é e como funciona um raw socket?**
📄 [Ex3_rawSocket.md](Ex3_rawSocket.md)  
Explicação teórica e prática sobre **raw sockets**, com um exemplo de **ping ICMP personalizado**.

---

### 🖥️ **4. Scanner de Portas**
📄 [Ex4_scanner.py](Ex4_scanner.py)  
Implementação de um **scanner de portas** usando sockets para verificar quais portas estão abertas em um host.

---

### 🔗 **5. Servidor TCP**
📄 [Ex5_svTCP.py](Ex5_svTCP.py)  
Implementação de um **servidor TCP** que aceita conexões de clientes e troca mensagens via sockets.

---

### 🔗 **6. Cliente TCP**
📄 [Ex6_clTCP.py](Ex6_clTCP.py)  
Implementação de um **cliente TCP** que se conecta ao servidor TCP da questão 5 para troca de mensagens.

---

### 📡 **7. Servidor UDP**
📄 [Ex7_svUDP.py](Ex7_svUDP.py)  
Implementação de um **servidor UDP**, aceitando pacotes de clientes sem estabelecer conexões.

---

### 📡 **8. Cliente UDP**
📄 [Ex8_clUDP.py](Ex8_clUDP.py)  
Implementação de um **cliente UDP** para se comunicar com o servidor UDP.

---

### 🌐 **9. Servidor HTTP**
📄 [Ex9_svHttp.py](Ex9_svHttp.py)  
Implementação de um **servidor HTTP** em Python, capaz de servir páginas HTML simples.

---

### 🌍 **10. Cliente HTTP**
📄 [Ex10_clHttp.py](Ex10_clHttp.py)  
Implementação de um **cliente HTTP** para se conectar e solicitar páginas ao servidor HTTP.

---

### 📁 **11. Servidor de Arquivos**
📄 [Ex11_svArqPython.py](Ex11_svArqPython.py)  
Implementação de um **servidor de arquivos** para upload e download de arquivos via sockets.

---

### 📁 **12. Cliente de Arquivos**
📄 [Ex12_clArqPython.py](Ex12_clArqPython.py)  
Implementação de um **cliente para envio e recebimento de arquivos** do servidor da questão 11.

---

### 🔐 **13. Protocolos de Criptografia em SSL/TLS**
📄 [Ex13_SSLLinux.py](Ex13_SSLLinux.py)  
Demonstração dos **protocolos de criptografia suportados** pelo módulo `ssl` instalado no Linux.

---

### 🔏 **14. Certificação de Segurança de Servidores HTTPS**
📄 [Ex14_reqHttps.py](Ex14_reqHttps.py)  
Aplicação em Python para **obter e verificar certificados SSL** de servidores HTTPS.

---

### 🔒 **15. Servidor HTTP com Socket Seguro (HTTPS)**
📄 [Ex15_svHttps.py](Ex15_svHttps.py)  
Modificação do servidor HTTP da questão 9 para usar **SSL/TLS**, garantindo comunicação segura.

---

### 🔑 **16. Cliente HTTPS**
📄 [Ex16_clHttps.py](Ex16_clHttps.py)  
Modificação do cliente HTTP para se conectar ao servidor HTTPS da questão 15, estabelecendo uma **conexão segura via TLS**.

---

## 📂 **Arquivos Adicionais**
- 📄 [index.html](index.html) → Página HTML usada pelo servidor HTTP.  
- 📄 [requirements.txt](requirements.txt) → Dependências do projeto.

