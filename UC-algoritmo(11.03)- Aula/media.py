nome = input("digite o nome completo do aluno: ")
matricula = int(input("digite a matrícula do aluno: "))
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))


media = (nota1 + nota2) / 2

print("\n relatório do aluno")
print("nome:", nome)
print("matrícula:", matricula)
print("nota 1:", nota1)
print("nota 2:", nota2)
print("média:", media)
