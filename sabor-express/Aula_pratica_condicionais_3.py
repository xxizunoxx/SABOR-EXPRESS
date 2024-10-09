# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
"""
dados_pessoais = [{'Nome' : 'Caique Camargo', 'Idade' : '31', 'Cidade' : 'São Paulo'},
                  {'Nome' : 'Rodrigo Goes', 'Idade' : '45', 'Cidade' : 'Minas Gerais'},
                  {'Nome' : 'Jiraya', 'Idade' : '60', 'Cidade' : 'Konoha'},
]

print(dados_pessoais)
"""
# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
"""
dados_pessoais = {'Nome' : 'Caique Camargo', 'Idade' : '31', 'Cidade' : 'São Paulo'}
print(dados_pessoais)

dados = input('Insira: ')
dados_pessoais['Idade'] = dados
dados_pessoais['Profissao'] = 'Analista de Sistemas'
del dados_pessoais['Cidade']
print(dados_pessoais)
"""
# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
"""
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)
"""
# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
"""
dados_pessoais = {'Nome' : 'Caique Camargo', 'Idade' : '31', 'Cidade' : 'São Paulo'}
if 'Nome' in dados_pessoais:
    print("A chave 'Nome' existe no dicionário.")
else:
    print("A chave 'Nome' não existe no dicionário.")
"""
# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
"""
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
"""