funcao inicio(){
        real valorCasa, salario, prestacao
        inteiro anos, meses

        escreva("Qual o valor da casa: ")
        leia(valorCasa)

        escreva("Qual o seu salario? ")
        leia(salario)
        
        escreva("Em quantos anos você deseja pagar?")
        leia(anos)

        meses=anos*12
        prestacao=valorCasa / meses 

        se(prestacao <= salario * 0.30) {`
       escreva("Parcelas de", parc," mensais; Emprestimo negado, o valor exede 30% do salário do comprador")
        }senao{
            escreva("Parcelas de", parc,"mensais; Emprestimo aprovado")
        }
}
