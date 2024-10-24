lista = [1,2,3,4,5,6]

n1 = lista[5]
n2 = lista[-1]
soma = n1+n2

lista.append(50)
lista.append('teste')

lista.remove(6)
lista.pop(2)


print(soma)

# lista.clear()
print(lista)


nova_lista = lista.copy()
print(nova_lista)

# insert

lista.insert(0, 10000)

print(lista)

lista2 = list(range(1, 151))


lista2.insert(30, 32)
print(lista2)


# contagem do valor dentro da lista

numero = int(input('Ache a quantidade do valor dentro da lista: '))

lista3 = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6]

print(lista3.count(numero))