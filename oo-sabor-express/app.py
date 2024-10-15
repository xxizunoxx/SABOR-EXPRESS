from modelos.restaurante import Restaurante

restaurante_gigante = Restaurante('Gigante Nordestino', 'Nordestina')
restaurante_gigante.receber_avaliacao('Caique', 9)
restaurante_gigante.receber_avaliacao('Natalia', 10)
restaurante_gigante.receber_avaliacao('Caue', 8)
restaurante_outback = Restaurante('Outback', 'Australiana')
restaurante_outback.receber_avaliacao('Jonatan', 6)
restaurante_outback.receber_avaliacao('João', 4)
restaurante_outback.receber_avaliacao('Rogerio', 9)
restaurante_mcdonalds = Restaurante('Mcdonalds', 'Fast Food')

restaurante_outback.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()