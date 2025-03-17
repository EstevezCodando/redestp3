import ssl
import socket
from datetime import datetime

def obter_certificado_ssl(hostname, porta=443):
    """
    Obtém e exibe informações detalhadas do certificado SSL de um servidor HTTPS.

    Args:
        hostname (str): Nome do host do servidor HTTPS.
        porta (int, opcional): Porta do servidor. Padrão é 443.
    """
    contexto = ssl.create_default_context()

    try:
        with socket.create_connection((hostname, porta), timeout=5) as conexao:
            with contexto.wrap_socket(conexao, server_hostname=hostname) as conexao_ssl:
                cert = conexao_ssl.getpeercert()

                # Extraindo informações do certificado
                nome_comum = dict(cert['subject'][0])['commonName']
                emissor = dict(cert['issuer'][0])['commonName']
                validade_inicio = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
                validade_fim = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                protocolo_tls = conexao_ssl.version()
                cipher_suite = conexao_ssl.cipher()[0]

                # Exibição das informações do certificado
                print(f"\n🔹 **Certificado SSL para:** {hostname}")
                print(f"🔹 Nome Comum (CN): {nome_comum}")
                print(f"🔹 Emitido por (CA): {emissor}")
                print(f"🔹 Validade: {validade_inicio.strftime('%d/%m/%Y')} até {validade_fim.strftime('%d/%m/%Y')}")
                print(f"🔹 Protocolo TLS em uso: {protocolo_tls}")
                print(f"🔹 Cipher Suite: {cipher_suite}")

                # Verificação de expiração
                hoje = datetime.utcnow()
                if validade_fim < hoje:
                    print("⚠️ O certificado está **EXPIRADO**!")
                else:
                    dias_restantes = (validade_fim - hoje).days
                    print(f"✅ O certificado é válido por mais {dias_restantes} dias.")

    except ssl.SSLError as e:
        print(f"❌ Erro SSL ao conectar-se a {hostname}: {e}")
    except socket.gaierror:
        print(f"❌ Erro: O domínio '{hostname}' não foi encontrado.")
    except socket.timeout:
        print(f"❌ Erro: Tempo limite de conexão esgotado para {hostname}.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    dominio = input("Digite o domínio HTTPS para verificar (ex: lms.infnet.edu.br): ")
    obter_certificado_ssl(dominio)
