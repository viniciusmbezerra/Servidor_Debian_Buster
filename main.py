import os
from gerar_arquivo import gerar_arquivo

os.system("apt install openssh-client openssh-server -y")
os.system("apt install bind9 bind9-doc -y")
os.system("apt install apache2 apache2-doc -y")

dados = {
    "DNS": "vinicius.com", 
    "SERIAL": "2022121601", 
    "IP_NS": "10.0.0.20", 
    "PREFIXO": "vinicius", 
    "PORTA_PADRAO": "20", 
    "PORTA_ROUTER": "1",
    "NETMASK": "255.255.255.0", 
    "GATEWAY": "10.0.0.1", 
    "NETWORK": "10.0.0.0", 
    "BROADCAST": "10.0.0.255",
    "IP_INVERSO": "0.0.10",
}

# PASTA_APP = os.path.dirname(__file__)
# arquivos = [
#     PASTA_APP+"\\arquivos\\interfaces",
#     PASTA_APP+"\\arquivos\\resolv.conf",
#     PASTA_APP+"\\arquivos\\sshd_config",
#     PASTA_APP+"\\arquivos\\db.DNS_EXAMPLE",
#     PASTA_APP+"\\arquivos\\db.IP_EXAMPLE",
#     PASTA_APP+"\\arquivos\\named.conf.local",
# ]

arquivos = [
    "/etc/network/interfaces",
    "/etc/resolv.conf",
    "/etc/ssh/sshd_config",
    "/etc/bind/db.DNS_EXAMPLE",
    "/etc/bind/db.IP_EXAMPLE",
    "/etc/bind/named.conf.local",
]

for arq in arquivos:
    gerar_arquivo(arq, dados)