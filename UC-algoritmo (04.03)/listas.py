nome1= "Ana"
nome2 = "Bruno"
nome3 = "Caio"

nomes = ["Ana", "Bruno", "Caio"]
print(nomes)

dados = ["Carol", 0, 1.70, True]
print(dados)
print(type(dados))
print(type(dados[0])) #str
print(type(dados[1])) #int
print(type(dados[2])) #float
print(type(dados[3])) #bool

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||

lista =["Cachorro", "Gato"]
print("Original: ", lista) 
lista.append("Coelho") #Add no fim da lista 
print("Atualizado: ", lista)

lista.insert(1, "Grilo") #add na posição determinada
print("Atualizado: ",lista)

lista.extend(["Macaco","ovelha"]) #add mais de um dado de uma vez
print("Lista final",lista)


