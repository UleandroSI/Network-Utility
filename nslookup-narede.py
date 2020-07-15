__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.1"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"

import socket
import time

# Abrir arquivo .txt que está na mesma pasta
arquivo = open("IPs.txt", "r")

# Leitura das linhas do arquivo de IPs
for linha in arquivo:
    ''' Para utilizar se pretender fazer nslookup pelo nome ao inves do IP
    addr = socket.gethostbyname('yahoo.com')
    print(addr)    '''
    while True:
    # Verifica se IP está registrado no DNS e trata o erro
        try:
            hostName = socket.gethostbyaddr(linha)
            print(hostName)
            print("O nome registrado para o IP {} e: {}".format(linha, hostName))
            break
        except socket.gaierror:
            print("srvdc não encontrou ",linha)
            #time.sleep(2.4)
            break

arquivo.close()
