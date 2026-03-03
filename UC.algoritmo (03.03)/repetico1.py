#𝔼𝕊𝕋ℝ𝕌𝕋𝕌ℝ𝔸 𝔻𝔼 ℝ𝔼ℙ𝔼𝕋𝕀ℂ̧𝔸̂𝕆
print("Olá, mundo!")
print("Olá. mundo!")
print("Olá, mundo!")
print("Olá, mundo!")

cont = 1 #contador 

while cont <=10: #Igual ao enquanto, quando o programador não sabe quantas vezes o programa vai rodar.
    print("Olá, mundo!")
    cont += 1 # É igual á: cont = cont + 1
print("FIM")

print(list(range(10))) #Range:sequência numérica.
print(list(range(1,10,2))) #sequencia numérica de dois em dois/ 1º:1-ínicio; 2º:10-término; 3º: 2- intervalo.

for cont in range(10): # para cada termo no intervalo de 1 a 10 imprima: "Olá, mundo!"
    print("Olá mundo")
print("Fim")

soma = 0 
for termo in range(1,11):
    soma += termo
print(soma)