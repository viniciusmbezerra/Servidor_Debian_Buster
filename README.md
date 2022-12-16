# Servidor_Debian_Buster

## Automatizando criação de arquivos

## ``Requisitos``

1. O Git deve estar instalado

```
apt install git
```

2. O Python 3.10 deve estar instalado

```
apt install python 3.10
```

## ``Execução``

1. Entrar em modo ROOT

```
su
password
```

2. Clonar este repositório

```
git clone https://github.com/viniciusmbezerra/Servidor_Debian_Buster.git
```

3. Executar Script

```
python3 main.py
```

## ``Funcionamento``

* Este Script instala o ssh o bind e o apache2

```
    apt install openssh-client openssh-server -y
    apt install bind9 bind9-doc -y
    apt install apache2 apache2-doc -y
```

* E cria e configura os seguintes arquivos do servidor Debian Buster
```
    /etc/network/interfaces

    /etc/resolv.conf

    /etc/ssh/sshd_config

    /etc/bind/db.DNS

    /etc/bind/db.IP_REVERSO
    
    /etc/bind/named.conf.local
```
