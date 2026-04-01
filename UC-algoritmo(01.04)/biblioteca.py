# Dicionario para armazenar os emprestimos
emprestimoAtivo = {}

#lista para armazenar o histórico de transição
historico = []

#Dicionario para armazenar os livros
catalogo = {}

def adicionarLivro(codigo,titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com codigo {codigo} já existe!")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor" : autor,
        "quantidade": quantidade 
    }

    print(f"Livro '{titulo}' adicionado com sucesso0")
    return True

#emprestar.py
codigo = {}

catalogo = {}

emprestimoAtivo = {}

historico = []

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro livro com codigo {codigo} já existe")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True

adicionarLivro("L1011", "Os sete maridos de Evelin Hugo", "JK Roling")
adicionarLivro("L1012", "O príncipe cruel", "Holly Black" )
adicionarLivro("L1013", "Imperfeitos", "Christina Lauren")

def emprestar_livro(codigo, nome_aluno):

    if codigo not in catalogo:
        print(f"Erro: Livro com {codigo} não encontrado")
        return False
    
    if catalogo[codigo]["quantidade"] <= 0:
        print(f"Erro: '{catalogo[codigo['titulo']]}' não encontrado!")
        return False
    
    livroAluno = conta_livros_aluno(nome_aluno)
    if livroAluno >= 2:
        print(f"Erro: {nome_aluno} já pegou a quantidade máxima")
        return False
    
    if codigo in emprestimos_ativos and nome_aluno in emprestimo_ativos[codigo]:
        print(f"Erro: {nome_aluno} já pegou este livro!")
        return False
    
    if codigo not in emprestimoAtivo:
        emprestimos_ativos[codigo] = []

#professora

codigo = {}

catalogo = {}

emprestimoAtivo = {}

historico = []

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro livro com codigo {codigo} já existe")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True

adicionarLivro("L1011", "Os sete maridos de Evelin Hugo", "JK Roling")
adicionarLivro("L1012", "O príncipe cruel", "Holly Black" )
adicionarLivro("L1013", "Imperfeitos", "Christina Lauren")

def emprestar_livro(codigo, nome_aluno):

    if codigo not in catalogo:
        print(f"Erro: Livro com {codigo} não encontrado")
        return False
    
    if catalogo[codigo]["quantidade"] <= 0:
        print(f"Erro: '{catalogo[codigo['titulo']]}' não encontrado!")
        return False
    
    livroAluno = conta_livros_aluno(nome_aluno)
    if livroAluno >= 2:
        print(f"Erro: {nome_aluno} já pegou a quantidade máxima")
        return False
    
    if codigo in emprestimos_ativos and nome_aluno in emprestimo_ativos[codigo]:
        print(f"Erro: {nome_aluno} já pegou este livro!")
        return False
    
    if codigo not in emprestimoAtivo:
        emprestimos_ativos[codigo] = []

    emprestimo_ativo[codigo].append(nome_aluno)

    catalogo[codigo]["quantidade"] -= 1

    historico.append({
        "tipo": "emprestimo"
        "Codigo": codigo[codigo]["titulo"],
        "aluno": nome_aluno
    })

    print(f"{nome_aluno} pegou '(catalogo[codigo]['titulo']' com sucesso)")
    return True
