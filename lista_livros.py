# ===================================================================================================


# FUNÇÕES:


def menu():
    r = 0

    while r not in [1,2,3]:

        print()
        print("Menu de Opções")
        print("1 - Dados dos Livros")
        print("2 - Sub-menu")
        print("3 - Sair")
        r = int(input("Escolha uma opção: "))
        print()
    
    return r

def menu_resposta_1():

    livros = {}
    
    i = 0

    while i < 10:

        nome = input(f"Informe o nome do livro {i+1}: ").lower()

        dados = {}
        dados["autor"] = input("autor: ").lower()
        dados["ano"] = int(input("ano: "))
        dados["paginas"] = int(input("N° páginas: "))

        livros[nome] = dados
        
        i += 1

    return livros  

def monta_sub_menu():
    r = 0
    while r not in [1,2,3,4,5,6]:

        print()
        print("Dados do sub-menu")
        print("1 - Buscar livros por ano;")
        print("2 - Excluir livro;")
        print("3 - Mostrar todos os livros;")
        print("4 - Alterar dados;")
        print("5 - Maior livro;")
        print("6 - Retorna ao menu principal;")
        r = int(input("Escolha uma opção: "))
        print()
    
    return r

def sub_1(livros):
    r = int(input("Ano: "))
    print(f"Os livros escritos no ano de {r} são: ")
    for chave in livros:
        if livros[chave]['ano'] == r:
            print(f"-{chave}")

def sub_2(livros):
    excluir = input("Qual o nome do livro que deseja excluir? ")

    for chave in list(livros):
        if chave == excluir:
            livros.pop(chave)

def sub_3(livros):
    print("Livros: ")
    print()
    for nome in livros:
        print(f"{nome}: ")
        for chave in livros[nome]:
            print(f"    {chave}: {livros[nome][chave]}")
        print()

def sub_4(livros):
    resposta = input('Informe o nome do livro: ')

    if resposta in livros:
        print(f"O livro selecionado foi: '{resposta}'\nInforme os seguintes dados: ")

        dados = {}
        dados["autor"] = input("    autor: ")
        dados["ano"] = int(input("    ano: "))
        dados["paginas"] = int(input("    N° páginas: "))

        livros[resposta] = dados
    
    else:
        print(f'O livros {resposta} não está presente na sua lista.\nPor favor ', end='')
        sub_4(livros)

def sub_5(livros):
    lista_pgs = []
    maior_n_pgs = 0

    for chave in livros:
        lista_pgs.append(livros[chave]["paginas"])

    maior_n_pgs = max(lista_pgs)

    print("O(s) livro(s) com maior número de pgs é(são): ")

    for chave in livros:
        if livros[chave]["paginas"] == maior_n_pgs:
            print(f"{chave}: ")
            for chave2 in livros[chave]:
                print(f"{chave2}: {livros[chave][chave2]}")


def sub_menu(livros):

    r = monta_sub_menu()

    if r == 1:

        sub_1(livros)
        sub_menu(livros)

    elif r == 2:

        sub_2(livros)
        sub_menu(livros)

    elif r == 3:

        sub_3(livros)
        sub_menu(livros)
    
    elif r == 4:

        sub_4(livros)
        sub_menu(livros)
    
    elif r == 5:

        sub_5(livros)
        sub_menu(livros)
    
    elif r == 6:

        menu()


# ===================================================================================================


# VARIAVEIS:


resposta_menu = menu()

# ex.: lista_livros = {"maze runer": {'autor': 'james dashner', 'ano': 2012, 'paginas': 480},
#                      "harry":      {'autor': 'jk rollin', 'ano': 1999, 'paginas': 620},
#                      "divergente": {'autor': 'Veronica Roth', 'ano': 2012, 'paginas': 455}}

lista_livros = {}


# ===================================================================================================


################# Programa Principal #################


while resposta_menu != 3:
        
    if resposta_menu == 1:
        lista_livros = menu_resposta_1()
        resposta_menu = menu()

    if resposta_menu == 2:
        sub_menu(lista_livros)
        resposta_menu = menu()


# ===================================================================================================