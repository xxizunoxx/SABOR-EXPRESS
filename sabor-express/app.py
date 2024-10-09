import os

restaurantes = [{'nome':'Gigante Nordestino', 'categoria':'Nordestina', 'ativo':False},
                {'nome':'Outback', 'categoria':'Australiana', 'ativo':True },
                {'nome':'Mc Donalds', 'categoria':'Fast-Food', 'ativo':False }
]

def exibir_nome_do_programa():
    '''Essa função é responsavél por exibir o nome do programa estilido'''

    print("""
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
""")

def exibir_opcoes():
    '''Essa função é responsavél por exibir as opções disponíveis no menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''

    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal

    Outputs:
    - Retorna ao menu principal

    '''

    input('\nAperte a tecla Enter para voltar ao menu principal\n')
    main()

def opcao_invalida():
    ''' Essa função é responsavél por imprimir a mensagem de opção inválida e volta ao menu principal

    Outputs:
    - Retorna ao menu principal

    '''

    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função é responsavél por exibir o subtitulo estilizado das opções selecionadas
    
    Inputs:
    - texto: str - O texto do subtítulo

    '''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsavél por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsavél por listar os restaurantes cadastrados

    Outputs:
     - Exibe a lista de restaurantes na tela

    '''

    exibir_subtitulo('Lista de restaurantes cadastrados')

    print(f'* {'Nome do restaurante'.ljust(20)} * {'Categoria'.ljust(20)} * {'Status'}')
    for x in restaurantes:
        nome = x['nome']
        categoria = x['categoria']
        status = 'ativado' if  x['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {status}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsavél por alternar o estado ativo/desativado do restaurante
    
    Inputs:
    - Nome do restaurante que deseja alterar
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação

    '''

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
    ''' Essa função é responsavél por escolher as opções listadas para o usúario
    
    Outputs:
    - Executa a opção escolhida pelo usuário

    '''
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
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()