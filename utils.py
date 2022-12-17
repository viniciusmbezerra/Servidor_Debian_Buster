def gerar_arquivo(caminho, dados):
    import os
    PASTA_APP = os.path.dirname(__file__)

    nome_arquivo = caminho.split("/")[-1]

    # lendo arquivo
    modelo = open(PASTA_APP+f"/arquivos/{nome_arquivo}", "r")
    texto = modelo.read()
    modelo.close()

    for chave in dados.keys():
        texto = texto.replace(chave, dados[chave])

    # alterando arquivo
    if nome_arquivo=="db.DNS_EXAMPLE":
        caminho = caminho.replace("DNS_EXAMPLE", dados["DNS"])
    if nome_arquivo=="db.IP_EXAMPLE":
        caminho = caminho.replace("IP_EXAMPLE", dados["IP_INVERSO"])

    arquivo = open(f"{caminho}", "w")
    arquivo.write(texto)
    arquivo.close()

    print(f"\n{caminho} -- configurado com sucesso")

def calc_dados_automaticos(dados):
    dados["PREFIXO"] = dados["DNS"].replace(".com", "")
    dados["IP_INVERSO"] = ".".join(dados["IP_ADDRESS"].split(".")[:-1][::-1])
    dados["PORTA_PADRAO"] = dados["IP_ADDRESS"].split(".")[-1]

    hosts = 0
    for oct in dados["NETMASK"].split("."):
        if oct == "255":
            hosts+=1

    salto = abs(256-int(dados["NETMASK"].split(".")[hosts]))

    host = int(dados["IP_ADDRESS"].split(".")[-1])
    for i in range(256//salto):
        ip = dados["IP_ADDRESS"].split(".")
        ip[-1] = str(0)
        ip[hosts] = str(i*salto)
        if host > i*salto and host < (i+1)*salto:
            dados["GATEWAY"] = ".".join(dados["IP_ADDRESS"].split(".")[:-1])+f".{i*salto+1}"
            dados["NETWORK"] = ".".join(dados["IP_ADDRESS"].split(".")[:-1])+f".{i*salto}"
            dados["BROADCAST"] = ".".join(dados["IP_ADDRESS"].split(".")[:-1])+f".{(i+1)*salto-1}"
    
    return dados