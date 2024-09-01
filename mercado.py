from typing import List, Dict
from time import sleep

from models.produto import Produto  # Importa a classe Produto do módulo models
from utils.helper import formata_float_str_moeda  # Importa uma função auxiliar para formatar valores em moeda

# Inicializa listas para armazenar os produtos disponíveis e o carrinho de compras
produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

# Função principal que inicia o sistema de compras
def main() -> None:
    menu()  # Chama o menu principal

# Função que exibe o menu e gerencia as opções do sistema
def menu() -> None:
    print('===================================')
    print('=========== Bem-vindo(a) ==========')
    print('===========  LF Shop   ==========')
    print('===================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())  # Lê a opção escolhida pelo usuário

    # Verifica a opção selecionada e chama a função correspondente
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)  # Sai do sistema
    else:
        print('Opção inválida!')
        sleep(1)
        menu()  # Retorna ao menu em caso de opção inválida

# Função para cadastrar um novo produto
def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    # Solicita ao usuário o nome e o preço do produto
    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    # Cria um novo produto e o adiciona à lista de produtos
    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()  # Retorna ao menu

# Função para listar todos os produtos cadastrados
def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()  # Retorna ao menu

# Função para adicionar um produto ao carrinho de compras
def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('================== Produtos Disponíveis ======================')
        for produto in produtos:
            print(produto)
            print('---------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())  # Lê o código do produto escolhido

        produto: Produto = pega_produto_por_codigo(codigo)  # Busca o produto pelo código

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        # Se o produto já está no carrinho, aumenta a quantidade
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()  # Retorna ao menu
                if not tem_no_carrinho:
                    # Se o produto não estava no carrinho, adiciona com quantidade 1
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()  # Retorna ao menu
            else:
                # Se o carrinho estava vazio, adiciona o primeiro produto
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()  # Retorna ao menu
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()  # Retorna ao menu
    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()  # Retorna ao menu

# Função para visualizar os produtos no carrinho
def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])  # Exibe o produto
                print(f'Quantidade: {dados[1]}')  # Exibe a quantidade
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()  # Retorna ao menu

# Função para fechar o pedido e calcular o valor total
def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])  # Exibe o produto
                print(f'Quantidade: {dados[1]}')  # Exibe a quantidade
                valor_total += dados[0].preco * dados[1]  # Calcula o valor total
                print('------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')  # Exibe o valor total formatado
        print('Volte sempre!')
        carrinho.clear()  # Limpa o carrinho após o pedido ser fechado
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()  # Retorna ao menu

# Função auxiliar para buscar um produto pelo código
def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto  # Retorna o produto que corresponde ao código
    return p

# Verifica se o script está sendo executado diretamente (e não importado como módulo)
if __name__ == '__main__':
    main()  # Chama a função principal para iniciar o sistema
