def calculadora():
 while True:

    print("[1] adição")
    print("[2] subitracao")
    print("[3] mutiplicação")
    print("[4] divisão")
    print("[0] sair")

    opcao = int(input("digite sua opção:"))

    a = float(input("digite um numero:"))
    b = float(input("digite um numero:"))

    match opcao:
      case 1:
        print(f"resltado: {a+b}")
      case 2:
         print(f"resltado: {a-b}")
      case 3:
         print(f"resltado: {a*b}")
      case 4:
          print(f"resltado: {a/b}")
      case 0:
        print("saindo...")
      case _:
        print("apção invalida")
    
calculadora()

 





