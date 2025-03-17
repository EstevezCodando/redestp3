# No linux a maneira mais simples é utilizando "openssl ciphers -v"
# No entanto o codigo abaixo tambem consegue exibir de maneira similar.
import ssl
ciphers = ssl.SSLContext(ssl.PROTOCOL_SSLv23).get_ciphers()
for cipher in ciphers:
    print(cipher['name']+" "+cipher['protocol'])