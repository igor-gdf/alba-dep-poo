# Classe Autor
class Autor:
    def __init__(self, nome: str, nacionalidade: str, data_nascimento: str):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__data_nascimento = data_nascimento

    def get_nome(self):
        return self.__nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def get_data_nascimento(self):
        return self.__data_nascimento

    # Métodos setters
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_nacionalidade(self, nacionalidade: str):
        self.__nacionalidade = nacionalidade

    def set_data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = data_nascimento

    def exibir_autor(self):
        return f'Nome: {self.__nome}, Nacionalidade: {self.__nacionalidade}, Data de Nascimento: {self.__data_nascimento}'

# Classe Livro
class Livro:
    def __init__(self, titulo: str, autor: Autor, ano_publicacao: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano_publicacao(self):
        return self.__ano_publicacao

    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_autor(self, autor: Autor):
        self.__autor = autor

    def set_ano_publicacao(self, ano_publicacao: int):
        self.__ano_publicacao = ano_publicacao

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionar_livro(self, livro: Livro):
        self.__livros.append(livro)

    def remover_livro(self, titulo: str):
        for livro in self.__livros:
            if livro.get_titulo().lower() == titulo.lower():
                self.__livros.remove(livro)
                return f'O livro "{titulo}" foi removido da biblioteca.'
        return f'O livro "{titulo}" não foi encontrado na biblioteca.'

    def buscar_livro(self, titulo: str):
        for livro in self.__livros:
            if livro.get_titulo().lower() == titulo.lower():
                return livro
        return None

    def listar_livros(self):
        if len(self.__livros) == 0:
            return 'Nenhum livro disponível na biblioteca.'
        lista_livros = ''
        for livro in self.__livros:
            lista_livros += f'Título: {livro.get_titulo()}, Autor: {livro.get_autor().get_nome()}, Ano: {livro.get_ano_publicacao()}\n'
        return lista_livros
