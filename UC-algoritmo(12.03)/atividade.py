
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

def calcularoperacao(n1,n2):
    soma = n1 + n2
    produto = n1 * n2
    return soma, produto
resultado_p , resultado = calcularoperacao(n1,n2) 

print(f"soma: {resultado}")
print(f"produto: {resultado_p}")

    

    