my_array = [1, 2, 3, 4, 'teste', False, True, 0.1]
my_number_array = [5, 8, 10, 9, 1, 2, 4, 15, 7]

# Exibindo Elementos de um Array
print(my_array)

# Exibindo Elemento em um índice específico
print(my_array[0])  # Exibe o primeiro elemento
print(my_array[len(my_array) - 1])  # Exibe o último elemento
print(my_array[-1])  # Também exibe o último elemento
print(my_array[-2])  # Exibe o penúltimo
print(my_array[-3])  # Exibe o antepenúltimo
print(my_array[-4])  # Números negativos trazem os elementos em ordem inversa
# Exibe os elementos: A partir da posição 2 até
# a posição 5(6 - 1)
print(my_array[2:6])
# print(my_array[100])  # Vai dar o erro list index out of range

# Para ordenar minha lista: sort() - Não posso usar com o primeiro array.
# Precisa ser um array numérico
# sorted() ordena, mas não modifica o array original
my_number_array_ordenado = sorted(my_number_array)
print('Atribuí o resultado de sorted a '
      'uma nova variável:', my_number_array_ordenado)

# sort() ordena e altera o array original
my_number_array.sort()
print('Meu Array Original modificado:', my_number_array)

# Inserindo valores em mey array
# Primeiro vamos ver a forma menos eficiente
my_number_array.insert(0, 999)  # inserindo 999 na posição 0
# O insert adiciona um elemento na posição fornecida e depois
# desloca TODOS os elementos que existiam a partir dessa posição
# para a direita - Muito Custoso
print('\ninsert(0, 999):', my_number_array)
# Para adicionar um item de forma rápida
# Adiciona o item na última posição - Sem deslocamento
# e, sem custo de processamento
my_number_array.append(456)  # Mais indicado, se depender de desempenho
print('append(456):', my_number_array)

# Para remover um item: array.remove('Aqui coloca o item, não o índice')
my_number_array.remove(10)
print('remove(10):', my_number_array)
# Lembrando que, fazendo o remove, vai haver um shift
# dos elementos para a esquerda. Isso pode ser um
# processo custoso
# Dependendo do caso, podemos fazer como abaixo
my_number_array[2] = None
print('Atribuindo None:', my_number_array)
# Durante o processamento, pode ser desconsiderado o None
# Isso vai tornar meu algoritmo cada vez mais rápido
# Posso usar o del também, mas tem o custo do shift
del my_number_array[2]
print('Usando o del:', my_number_array)
