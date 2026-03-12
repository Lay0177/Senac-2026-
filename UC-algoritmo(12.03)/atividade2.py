horas = float(input("Quanto por hora você recebe? "))
valor = float(input("Quantas horas trabalhadas: "))

def calcularsalario(horas,valor):
    resultado = horas * valor
    return resultado
resultado_p , resultado = calcularsalario(horas,valor) 