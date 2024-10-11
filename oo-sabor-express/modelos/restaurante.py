class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}' 

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'nome: {restaurante.nome.ljust(20)} | categoria: {restaurante.categoria.ljust(20)} | Status: {restaurante.ativo}')

restaurante_gigante = Restaurante('Gigante Nordestino', 'Nordestina')
restaurante_outback = Restaurante('Outback', 'Australiana')

Restaurante.listar_restaurantes()
