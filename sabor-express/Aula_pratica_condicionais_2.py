# 1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

"""
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['emy','gui','lais','mari']
lista_de_anos = [1999,2023]
"""

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
"""
lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in lista_teste:
    print(f'.{x}')
"""

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
"""
valor = 0

for i in range(1, 11, 2):
    print(i)
    valor += i
print(valor)
"""
# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
"""
for i in range(10, 0, -1):
    print(f'.{i}')
"""

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um número: '))

for i in range(0, 11, 1):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado} ')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
