from modelos.restaurante import Restaurante

restaurante_gigante = Restaurante('Gigante Nordestino', 'Nordestina')
restaurante_gigante.receber_avaliacao('Caique', 4)
restaurante_gigante.receber_avaliacao('Natalia', 5)
restaurante_gigante.receber_avaliacao('Caue', 3.5)
restaurante_outback = Restaurante('Outback', 'Australiana')
# restaurante_outback.receber_avaliacao('Jonatan', 2)
# restaurante_outback.receber_avaliacao('João', 4)
# restaurante_outback.receber_avaliacao('Rogerio', 4.5)
restaurante_mcdonalds = Restaurante('Mcdonalds', 'Fast Food')

restaurante_outback.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()