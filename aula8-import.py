import random
numero_aleatorio = random.randint(1,2)
print(numero_aleatorio)
chute = int(input('Digite um numero de 1 a 2: '))

if numero_aleatorio == chute:
    print('você acertou em cheio')
    print('o numero é 1')
else: 
    print('voce errou')
    print('o numero era', numero_aleatorio)

    