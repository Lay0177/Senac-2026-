programa {
    funcao inicio () {
        inteiro n, soma,contador
            contador = 1
            soma = 0
            
            escreva("Digite um número: ")
            leia(n)


            enquanto (contador <= n) {
                soma = soma + contador
                contador = contador +1
            }

            escreva("A soma de 1 até ", n, "é: ", soma)


}
}