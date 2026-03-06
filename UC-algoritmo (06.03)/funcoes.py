notas = {7.5, 8.0, 9.5, 6.0, 8.5}
print("Notas: ", notas)

print("Menor: ", min(notas)) #Min:Menor número
print("Maior: ", max(notas)) #Max: Maior número
print("Soma: ", sum(notas))  #Sum: Média
print("Média:" ), sum(notas) / len(notas) #len: contagem de de gente da lista

nomes = ["Adriana", "Breno", "Carla", "Daniel"]

#Apenas o elemento
print("Usando FOR simples: ")
for nome in nomes: #for: para; in: um lugar
  print(f"Olá, {nome}!")

#índice e elemento
print ("\n Usando enumerate: ")
for indice, nome in enumerate(nomes): 
  print(f"posição {indice}:{nome}")


original=["A", "B", "C"] 
copia = list(original)

print("Original: ")
print("Cópia: ", copia)
print("São iguais: ", original == copia)

copia.append("D")
print("Original: ", original)
print(  "Cópia", copia)
print( "São iguais: ", original==copia)