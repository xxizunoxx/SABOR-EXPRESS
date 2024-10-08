import os

#Função para exibir nome do programa.
def exibir_nome_do_programa():
    print("""
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
""")

# Função para exibir opções do programa.
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

# Função para finalizar o app e limpar o terminal.
def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

# Função para escolher as opções.
def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: ')) # Variável tipada para definir a opção escolhida.

    match opcao_escolhida:
        case 1:
            print('Adicionar restaurante\n')
        case 2:
            print('Listar restaurantes\n')
        case 3:
            print('Ativar restaurante\n')
        case 4:
            print('Finalizar app\n')
        case _:
            print('Opção inválida!\n')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()