aluno = {}

aluno["nome"] = input("Qual o nome do aluno: ")
aluno["nota1"] = float("Qual a nota 1 do aluno: ")
aluno["nota2"] = float("Qual a nota 2 do aluno: ")

media = (aluno["nota1"] + aluno["nota 2"]) / 2

if media >= 7:
    print("passou")
elif media >= 5:
    print("média")
else:
    print("reprovou")

print("\n Dados")
print("Nome: ", aluno["nome"])
print("Média do ano", aluno["media"])
