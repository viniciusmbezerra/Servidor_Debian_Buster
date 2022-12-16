def gerar_arquivo(caminho, dados):
    import os
    PASTA_APP = os.path.dirname(__file__)

    nome_arquivo = caminho.split("/")[-1]

    modelo = open(caminho, "r")
    texto = modelo.read()
    modelo.close()

    for chave in dados.keys():
        texto = texto.replace(chave, dados[chave])

    try:
        arquivo = open(f"{caminho}", "w")
        arquivo.write(texto)
        arquivo.close()
    except:
        if nome_arquivo=="DNS_EXAMPLE":
            caminho = caminho.replace("DNS_EXAMPLE", dados["DNS"])
        if nome_arquivo=="IP_EXAMPLE":
            caminho = caminho.replace("IP_EXAMPLE", dados["IP_INVERSO"])
        
        arquivo = open(f"{caminho}", "a")
        arquivo.write(texto)
        arquivo.close()
    