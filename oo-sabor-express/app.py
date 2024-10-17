from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_gigante = Restaurante('Gigante Nordestino', 'Nordestina')
bebida_suco = Bebida('Suco de Manga', 5.0, 'Grande')
prato_xiquexique = Prato('Xique Xique', 190.00, 'Risoto de camarão')
restaurante_outback = Restaurante('Outback', 'Australiana')
restaurante_mcdonalds = Restaurante('Mcdonalds', 'Fast Food')

restaurante_outback.alternar_estado()

def main():
    print(bebida_suco)
    print(prato_xiquexique)

if __name__ == '__main__':
    main()