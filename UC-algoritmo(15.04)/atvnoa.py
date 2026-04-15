def media(): 
    notas=[]#lista
    try:    
        for i in range (1,4):
            nota=float(input(f"Digite sua nota {i}:"))
            notas.append(nota)

        media= sum(notas) / len(notas) #len: quantidade de valores pra lista
        print(f"A média final é: {media: .2f}") #sum: soma ; #2f: aparecer só até duas casas depois da vírgula

    except ValueError:
      print("digite somente numeros")

    except ZeroDivisionError: #Se a lista tiver zero
        print("Sem notas!")

media() #Chamar a função