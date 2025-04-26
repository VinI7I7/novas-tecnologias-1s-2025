def estatisticas(dados, campo):
    valores = [linha[campo] for linha in dados]
    total = sum(valores)
    media = total/len(valores)
    return {"media":media,"min":min(valores),"max":max(valores)}