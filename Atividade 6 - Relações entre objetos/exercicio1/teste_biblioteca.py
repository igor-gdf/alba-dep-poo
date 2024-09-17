from biblioteca import Autor
from biblioteca import Livro
from biblioteca import Biblioteca

def menu():
    biblioteca = Biblioteca()
    while True:
        print('\n==== Menu ====')
        print('1. Adicionar Livro')
        print('2. Remover Livro')
        print('3. Buscar Livro')
        print('4. Listar Livros')
        print('5. Sair')
        
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            titulo = input('Digite o título do livro: ')
            nome_autor = input('Digite o nome do autor: ')
            nacionalidade_autor = input('Digite a nacionalidade do autor: ')
            data_nascimento_autor = input('Digite a data de nascimento do autor: ')
            ano_publicacao = int(input('Digite o ano de publicação: '))

            autor = Autor(nome_autor, nacionalidade_autor, data_nascimento_autor)
            livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionar_livro(livro)
            print(f'O livro "{titulo}" foi adicionado à biblioteca.')

        elif opcao == '2':
            titulo = input('Digite o título do livro a ser removido: ')
            print(biblioteca.remover_livro(titulo))

        elif opcao == '3':
            titulo = input('Digite o título do livro que deseja buscar: ')
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                print(f'Livro encontrado: {livro.get_titulo()}, Autor: {livro.get_autor().get_nome()}, Ano: {livro.get_ano_publicacao()}')
            else:
                print('Livro não encontrado.')

        elif opcao == '4':
            print('\nLista de Livros Disponíveis:')
            print(biblioteca.listar_livros())

        elif opcao == '5':
            print('Saindo...')
            break

        else:
            print('Opção inválida, tente novamente.')

if __name__ == '__main__':
    menu()