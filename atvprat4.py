lista = []
codigo = 0  # Numeração que será atribuída aos futuros cadastros


def cadastrarProduto(cod):
    print("Você Selecionou a Opção de Cadastrar Produtos!")
    print("Código do Produto: {}".format(cod))
    nome = input("Digite o Nome do Produto: ")
    fab = input("Digite o Nome do Fabricante do Produto: ")
    valor = float(input("Digite o Valor (R$) do Produto: "))
    produto = {'Código': cod, 'Nome': nome, 'Fabricante': fab, 'Valor': valor}  # Dicionário que guarda as informações..
    # do produto.
    lista.append(produto.copy())  # Comando para guardar o dicionário criado acima na lista de produtos


def consultarProduto():
    print("Você Selecionou a Opção de Consultar Produtos!")
    while True:
        option = input("Escolha a Opção Desejada:\n"
                       "1) Consultar Todos os Produtos\n"
                       "2) Consultar Produto por Código\n"
                       "3) Consultar Produto(s) por Fabricante\n"
                       "4) Retornar\n"
                       ">> ")
        if option == "1":
            for produtos in lista:  # Seleciona cada dicionário (produto) inserido na lista
                for key, value in produtos.items():  # Seleciona cada conjunto de informações de determinado produto
                    print("{} : {}".format(key, value))  # Imprime as informações de forma ordenada (chave : valor)
        elif option == "2":
            consulta = int(input("Digite o Código do Produto: "))
            for produtos in lista:  # Seleciona cada dicionário (produto) inserido na lista
                if produtos['Código'] == consulta:   # Verifica até encontrar o código que coincida com a consulta
                    for key, value in produtos.items():  # Seleciona cada conjunto de informações de determinado produto
                        print("{} : {}".format(key, value))  # Imprime as informações de forma ordenada (chave : valor)
        elif option == "3":
            consulta = input("Digite o Fabricante do Produto: ")
            for produtos in lista:
                if produtos['Fabricante'] == consulta:  # Verifica até encontrar fabricantes que coincidam com consulta
                    for key, value in produtos.items():
                        print("{} : {}".format(key, value))
        elif option == "4":
            return
        else:
            print("Opção Inválida!")
            continue


def removerProduto():
    print("Você Selecionou a Opção de Remover Produtos!")
    remove = int(input("Digite o Código do Produto a ser Removido: "))
    for produtos in lista:  # Seleciona cada dicionário (produto) inserido na lista
        if produtos['Código'] == remove:  # Verifica até encontrar o código que coincida com o código digitado em remove
            lista.remove(produtos)  # Remove da lista o respectivo produto


print("Bem-vindo ao Controle de Estoque da Mercearia do Fulano")
while True:
    menu = input("Escolha a Opção Desejada:\n"
                 "1) Cadastrar Produtos\n"
                 "2) Consultar Produtos\n"
                 "3) Remover Produto\n"
                 "4) Sair\n"
                 ">> ")
    if menu == "1":
        codigo += 1
        cadastrarProduto(codigo)
    elif menu == "2":
        consultarProduto()
    elif menu == "3":
        removerProduto()
    elif menu == "4":
        print("Programa Finalizado!")
        break
    else:
        print("Opção Inválida!")
        continue
