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

    if opcao_escolhida == 1:
        print('Cadastrar restaurante\n')
    elif opcao_escolhida == 2:
        print('Listar restaurante\n')
    elif opcao_escolhida == 3:
        print('Ativar restaurante\n')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()