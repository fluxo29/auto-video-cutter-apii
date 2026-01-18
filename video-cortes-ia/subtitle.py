def gerar_blocos_com_tempo(inicio, fim, texto, max_palavras=3):
    palavras = texto.split()
    duracao_total = fim - inicio

    if len(palavras) == 0:
        return []

    tempo_por_bloco = duracao_total / max(1, len(palavras) // max_palavras)

    blocos = []
    tempo_atual = 0

    for i in range(0, len(palavras), max_palavras):
        bloco_texto = " ".join(palavras[i:i+max_palavras])

        blocos.append({
            "texto": bloco_texto,
            "inicio": tempo_atual,
            "fim": tempo_atual + tempo_por_bloco
        })

        tempo_atual += tempo_por_bloco

    return blocos
