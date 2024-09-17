#produto
class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_preco(self, preco: float):
        self.__preco = preco

    def set_quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    def exibir_produto(self):
        return f'Produto: {self.__nome}, Preço: {self.__preco}, Quantidade: {self.__quantidade}'
#venda

class Venda:
    def __init__(self, data_venda: str):
        self.__produtos = []
        self.__data_venda = data_venda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos

    def get_data_venda(self):
        return self.__data_venda

    def get_total(self):
        return self.__total

    def adicionar_produto(self, produto: Produto):
        self.__produtos.append(produto)

    def remover_produto(self, nome: str):
        for produto in self.__produtos:
            if produto.get_nome().lower() == nome.lower():
                self.__produtos.remove(produto)
                return f'O produto "{nome}" foi removido da venda.'
        return f'O produto "{nome}" não foi encontrado na venda.'

    def calcular_total(self):
        self.__total = sum(produto.get_preco() * produto.get_quantidade() for produto in self.__produtos)
        return self.__total

    def listar_produtos(self):
        if len(self.__produtos) == 0:
            return 'Nenhum produto adicionado à venda.'
        lista_produtos = '\n'.join([produto.exibir_produto() for produto in self.__produtos])
        return lista_produtos
