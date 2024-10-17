from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_gigante = Restaurante('Gigante Nordestino', 'Nordestina')
bebida_suco = Bebida('Suco de Manga', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_xiquexique = Prato('Xique Xique', 190.00, 'Risoto de camarão')
prato_xiquexique.aplicar_desconto()
restaurante_gigante.adicionar_no_cardapio(bebida_suco)
restaurante_gigante.adicionar_no_cardapio(prato_xiquexique)
restaurante_outback = Restaurante('Outback', 'Australiana')
restaurante_mcdonalds = Restaurante('Mcdonalds', 'Fast Food')


restaurante_outback.alternar_estado()

def main():
    restaurante_gigante.exibir_cardapio

if __name__ == '__main__':
    main()
