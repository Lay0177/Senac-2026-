def div(a,b):
    try:
        return a / b
        
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
        return 0
    
print(f"Resultado: {div(10, 0)}")




def soma(a,b):

    try:
        return a + b
        
    except TypeError:
        print("Entrada inválida")
        return 0
res1 = soma(10, 20)
print(f"Resultado: {res1}")
