paciente = {}

paciente["nome"] = input("Qual o seu pai: ")
paciente["idade"] = int(input("Quantos anos você tem: "))
paciente["Peso"] = float(input("Digite seu peso(kg): "))
paciente["altura"] = float(input("Qual a sua altura: "))

imc = paciente ["peso"] / (paciente['altura']** 2)

paciente["imc"] = imc

print("\n Dados")
print("Nome: ", paciente["nome"])
print("Idade: ", paciente["idade"])
print("Peso: ", paciente["peso"])
print("Altura: ",paciente["altura"])
print("IMC: ", round(paciente["altura"], 2))

