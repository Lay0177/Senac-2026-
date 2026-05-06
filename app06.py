from flask import Flask, render_template

app = Flask(__name__)

#Questão3
@app.route('/arearestrita/<int:id>')
def arearestrita(id):
  if id == 1:
     return "Acesso bloqueado (cadeado fechado)"
  else:
      return "Acesso liberado (cadeado aberto"
  
#questao4
@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f"O produto {nome} custa R${preco:.2f}."

#questao5
@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    resultado = (palavra + " ") * vezes
    return resultado.strip()

if __name__ == '__main__':
    app.run(debug=True)