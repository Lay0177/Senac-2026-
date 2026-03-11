contato = {
    "@kellykey": "Kelly, Key",
    "@paola": "Paolla",
    "@sheron": "Sheron",
    "@bruna": "Bruna"
}

print("Chaves: ")
for insta in contato.keys():
  print(insta) 

print("/n Valores: ")
for nome in contato.values():
  print(nome)

print("\n Pares: ")
for insta, nome in contato.items():
   print(f"{insta} --> {nome}")

contato ={
   "@camila": 1.70,
   "@paola": 1.80,
   "@Sheron": 1.55,
   "bruna": 1.69
}

print("Ordenando por chaves: ")
for insta in sorted(contato.keys()):
   print(f"{insta} --> {contato[insta]:.2f}m")

from operator import itemgetter
print("\n Ordenado por valor (altura): ")
for insta, estatura in sorted(contato.items(), key = itemgetter(1)):
    print(f"{insta} --> {estatura:.2f}m")
