saldo = float(input("Qual seu saldo?"))
saque = float(input("Qual seu saque?"))

def Contabanco(saldo,saque):
    #Classificação
    if  saque > saldo:
        return "Saldo insuficiente"
    elif saque <= saldo:
      taxa = saque > 1000
      saldo = saque * 0.02
    else:
        return "Sem taxa"
    
saldorestante= saldo - saque

print(saldorestante)

print(Contabanco(saldo, saque))