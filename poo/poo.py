class Veiculo:
    def movimentar(self):
        print('\nVeículo em movimento\n')

    def __init__(self, fabricante, modelo, ano, cor, tipo_combustivel):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.ano = ano
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.__numero_registro = None

    def set_numero_registro(self, registro):
        self.__numero_registro = registro

    def get_numero_registro(self):
        return self.__numero_registro

    def get_fabricante(self):
        print(f'Fabricante: {self.__fabricante}')

    def get_modelo(self):
        print(f'Modelo: {self.__modelo}')


class Carro(Veiculo):
    def movimentar(self):
        print(f'\nCarro em movimento\n')


class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'\nMotocicleta em movimento\n')


class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria, qtd_assentos, ano, cor, tipo_combustivel):
        self.__categoria = categoria
        self.__qtd_assentos = qtd_assentos
        super().__init__(fabricante, modelo, ano, cor, tipo_combustivel)

    def get_categoria(self):
        return self.__categoria

    def get_qtd_assentos(self):
        return self.__qtd_assentos

    def movimentar(self):
        print('\nAvião em movimento\n')


if __name__ == '__main__':
    veiculo = Veiculo('Volkswagen', 'Polo', 2024, 'Preta', 'Flex')
    veiculo.movimentar()
    veiculo.get_fabricante()
    veiculo.get_modelo()
    veiculo.set_numero_registro('123456-x')
    print(f'Nº de registro: {veiculo.get_numero_registro()}')

    carro = Carro('GM', 'Onix', 2015, 'Prata', 'Flex')
    carro.movimentar()
    carro.get_fabricante()
    carro.get_modelo()

    moto = Motocicleta('BMW', 'S 1000 RR', 2022, 'Branca e Preta', 'Gasolina')
    moto.movimentar()
    moto.get_fabricante()
    moto.get_modelo()

    aviao = Aviao('Boeing', '747', 'Comercial', 660,
                  2000, 'Branca e Azul', 'Querosene')

    aviao.movimentar()
    aviao.get_fabricante()
    aviao.get_modelo()
    print(f'Categoria do avião: {aviao.get_categoria()}')
    print(f'\nAno de fabricação do avião: {aviao.ano}')
    print(f'\nQtde. assentos: {aviao.get_qtd_assentos()}')
