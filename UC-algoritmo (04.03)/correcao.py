#Correção - Atividade:SOMA E PRODUTO(03/03) -
#1- ACERTEI;
#2- ACERTEI;
#DO CELULAR
#3- ACERTEI;
#4- ACERTEI

#Questão 1

numero1 = float(input("Digite o 1º número:"))
numero2 = float(input("Digite o 2º número:"))

soma = numero1 + numero2
produto = numero1 * numero2

print("Soma:", soma)
print("Soma:", produto)

#Questão 2


if (numero % 2 == 0):
    resultado = numero0  ** 2

else:
    resultado = numero ** 3

    print("Resultado", resultado)

    #Questão 3

    usuario = input("Digite seu user:")
    senha = input("Digite sua senha:")

    if (usuario == "procopio" and senha == "1234") or (usuario == "paiva" and senha == "54321")
         print("Seja bem-vindo!")

    else: 
         print("Usuario e senha não conferem.")


#Questão 4

nome = input("Digite seu nome:")
senhaCorreta ="123456"

tentativa = 3

while tentativa > 3:
    senha = input("Digite sua senha:")

    if senha == senhaCorreta :
        print(f"Olá,{nome}! Seja bem-vindo!")
        break
    else:
        tentativa -= 1

        if tentativa == 2:
            print("Senha errada! Você tem 2 tentativas")
        elif tentativa == 1:
               print("Senha errada! Você tem 1 tentativa")
        else:
            print("Senha bloqueada")

