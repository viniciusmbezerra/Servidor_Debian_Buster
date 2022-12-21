import os
from utils import gerar_arquivo, calc_dados_automaticos
from datetime import date

os.system("apt install openssh-client openssh-server -y")
os.system("apt install bind9 bind9-doc -y")
os.system("apt install apache2 apache2-doc -y")
os.system("apt-get install dnsutils -y")

dados = {
    # dados manuais
    "DNS": "", 
    "IP_ADDRESS": "",
    "NETMASK": "",
    # dados automáticos
    "GATEWAY": "",
    "NETWORK": "", 
    "BROADCAST": "",
    "PREFIXO": "",
    "PORTA_PADRAO": "",
    "PORTA_ROUTER": "1",
    "IP_INVERSO": "",
    "SERIAL": f'{date.today().year}{date.today().month}{date.today().day}01',
}

arquivos = [
    "/etc/network/interfaces",
    "/etc/resolv.conf",
    "/etc/ssh/sshd_config",
    "/etc/bind/db.DNS_EXAMPLE",
    "/etc/bind/db.IP_EXAMPLE",
    "/etc/bind/named.conf.local",
    "/etc/apache2/conf-available/security.conf",
]

os.system("clear")

print("\nINFORME OS SEGUINTES DADOS ABAIXO:\n")

for i in range(0,3):
    chave = list(dados.keys())[i]
    dados[chave] = input(f"{chave}: ")

dados = calc_dados_automaticos(dados)

print("\nOs dados abaixo são gerados automaticamente, você pode altera-los.\nSe não quiser alterar aperte enter.\n")
for i in range(3, 11):
    chave = list(dados.keys())[i]
    aux = input(f"{chave} (valor atual= {dados[chave]}): ")
    if len(aux):
        dados[chave] = aux

os.system("clear")

for arq in arquivos:
    gerar_arquivo(arq, dados)

print("\nConfiguração concluída com sucesso!\n")
