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
