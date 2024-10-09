import os

restaurantes = [{'nome':'Gigante Nordestino', 'categoria':'Nordestina', 'ativo':False},
                {'nome':'Outback', 'categoria':'Australiana', 'ativo':True },
                {'nome':'Mc Donalds', 'categoria':'Fast-Food', 'ativo':False }
]

def exibir_nome_do_programa():
    '''Essa função é responsavél por exibir o nome do programa'''

    print("""
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
""")

def exibir_opcoes():
    '''Essa função é responsavél por exibir as opções'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsavél por finalizar o app'''

    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    '''Essa função é responsavél por voltar ao menu principal'''

    input('\nDigite uma tecla para voltar ao menu principal\n')
    main()

def opcao_invalida():
    '''Essa função é responsavél por imprimir a mensagem de opção invalida'''

    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função é responsavél por exibir o subtitulo das opções selecionadas'''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsavél por cadastrar um novo restaurante'''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsavél por listar os restaurantes cadastrados'''

    exibir_subtitulo('Lista de restaurantes cadastrados')

    print(f'* {'Nome do restaurante'.ljust(20)} * {'Categoria'.ljust(20)} * {'Status'}')
    for x in restaurantes:
        nome = x['nome']
        categoria = x['categoria']
        status = 'ativado' if  x['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {status}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsavél por alternar o estado do restaurante'''

    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com successo.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsavél por escolher as opções listadas para o usúario'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) # Variável tipada para definir a opção escolhida.

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()