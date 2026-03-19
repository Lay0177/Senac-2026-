pontos = float(input("Quantos pontos você ganhou?"))
derrotas = float(input("Quantos derrotas você ganhou?"))

def rankjogador(pontos,derrotas):
    pontosfinais = derrotas - (pontos * 10)

    #Classificação
    if pontosfinais < 0:
        return "Banido"
    elif pontos < 100:
        return "Bronze"
    elif pontos < 300:
        return "Prata"
    elif pontos < 600:
        return "Ouro"
    elif pontos <= 600:
        return "Diamante" 
    else:
        return "Tente outra vez!"
    
print(rankjogador(pontos, derrotas))