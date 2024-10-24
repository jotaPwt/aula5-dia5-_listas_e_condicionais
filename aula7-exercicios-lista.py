# **Exercício 1:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

lista_1a20 = list(range(1, 21, 2))
print(lista_1a20)

# **Exercício 2:** Escreva um programa que use a função `range()` para gerar os múltiplos de 5 em 5 até 50, em seguida, calcule e imprima a soma desses múltiplos.
lista_5em5 = list(range(5, 50, 5))

print(lista_5em5)

soma_lista = sum(lista_5em5)

print('A soma dessa lista é {}' .format(soma_lista))

# # **Exercício 1:** Crie uma lista chamada pessoas que contenha os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.

pessoas = ['pessoa1', 'pessoa2', 'pessoa3', 'pessoa4', 'pessoa5']

print(pessoas)


# # **Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.

numeros = [1,2,3,4,5,6]
print(numeros)
insira = int(input('Digite um numero para acrecentar na sua lista: '))
numeros.insert(5, insira)
numeros.append(insira)
print(numeros)


# # **Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.

numeros.append(9)
numeros.insert(0,8)
print(numeros)

 # **Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.

numeros.pop(4)
print(numeros)

# # **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.

carros = ['corsa', 'fusca', 'lancer']

print(carros[0], numeros[0])
print(carros[2], numeros[2])