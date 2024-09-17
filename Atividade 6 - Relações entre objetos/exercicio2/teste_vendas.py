from sistema_de_vendas import Produto
from sistema_de_vendas import Venda

def menu():
    data_venda = input('Digite a data da venda (dd/mm/aaaa): ')
    venda = Venda(data_venda)

    while True:
        print('\n==== Menu ====')
        print('1. Adicionar Produto')
        print('2. Remover Produto')
        print('3. Listar Produtos')
        print('4. Mostrar Total da Venda')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Digite o nome do produto: ')
            preco = float(input('Digite o preço do produto: '))
            quantidade = int(input('Digite a quantidade do produto: '))

            produto = Produto(nome, preco, quantidade)
            venda.adicionar_produto(produto)
            print(f'O produto "{nome}" foi adicionado à venda.')

        elif opcao == '2':
            nome = input('Digite o nome do produto a ser removido: ')
            print(venda.remover_produto(nome))

        elif opcao == '3':
            print('\nProdutos na venda:')
            print(venda.listar_produtos())

        elif opcao == '4':
            total = venda.calcular_total()
            print(f'Total da venda: R$ {total:.2f}')

        elif opcao == '5':
            print('Saindo...')
            break

        else:
            print('Opção inválida, tente novamente.')

if __name__ == '__main__':
    menu()