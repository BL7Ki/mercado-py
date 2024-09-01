from utils.helper import formata_float_str_moeda  # Importa uma função auxiliar para formatar valores em moeda

class Produto:
    contador: int = 1  # Atributo de classe que servirá para gerar códigos únicos para os produtos

    def __init__(self: object, nome: str, preco: float) -> None:
        # Atributos de instância
        self.__codigo: int = Produto.contador  # Atribui o valor atual do contador como código do produto
        self.__nome: str = nome  # Nome do produto
        self.__preco: float = preco  # Preço do produto
        Produto.contador += 1  # Incrementa o contador para garantir que o próximo produto tenha um código único

    # Método para acessar o código do produto
    @property
    def codigo(self: object) -> int:
        return self.__codigo

    # Método para acessar o nome do produto
    @property
    def nome(self: object) -> str:
        return self.__nome

    # Método para acessar o preço do produto
    @property
    def preco(self: object) -> float:
        return self.__preco

    # Método especial que define como o objeto será representado como string
    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_str_moeda(self.preco)}'
        # Retorna uma string formatada com o código, nome e preço do produto formatado em moeda
