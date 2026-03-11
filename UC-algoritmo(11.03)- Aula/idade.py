idade = int(input("digite a idade do atleta: "))

if idade < 12:
    categoria = "infantil"
elif idade >= 12 and idade < 18:
    categoria = "juvenil"
elif idade >= 18 and idade < 60:
    categoria = "adulto"
else:
    categoria = "sênior"

print("\n categoria:", categoria)
print("bem-vindo à competição, atleta da categoria", categoria + "!")
