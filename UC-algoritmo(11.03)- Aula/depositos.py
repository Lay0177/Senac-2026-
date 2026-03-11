quantidade_transacoes = 0

while True:
    valor = float(input("digite o valor do depósito (0 para encerrar): "))
    
    if valor == 0:
     break  # encerra o loop
    
    total_depositos += valor
    quantidade_transacoes += 1

print("\ntotal de depósitos: r$", total_depositos)
print("quantidade de transações:", quantidade_transacoes)
