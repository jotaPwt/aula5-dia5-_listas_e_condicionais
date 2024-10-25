# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

num = int(input('digite um numero -> '))
if num > 0:
    print('o numero é positivo')
else:
    print('o numero é negativo')

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade = int(input('Digite sua idade: '))
if idade >= 16:
    print('pode votar')
else:
    print('não pode votar')

# 3*

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

parimpar = int(input('Digite um número par ou ímpar: '))

if parimpar % 2 == 0:
    print('o número é par')
else:
    print('o número é impar')
# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

l1 = int(input('digite um lado: '))
l2 = int(input('digite um lado: '))
l3 = int(input('digite um lado: '))

if l1 == l2 == l3:
    print('equilatero')
elif l1 == l2 and l2 != l3 or l1 == l3 and l2!= l3:
    print('isoceles')
else:
    print('escaleno')

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

# Determine se um número é múltiplo de 5 e 7.

numero = int(input('digite um numero'))

if numero % 5 == 0 or numero % 7 == 0:
    print('é multiplo')
else: 
    print('Não é')  



# 6*

# Verifique se um número é positivo e maior que 10

numb = int(input('digite um numero: '))

if numb > 0 and numb > 10:
    print('é as duas condiçoes')
else:
    print('não é')

# 7*

# Verifique se um número é divisível por 3 ou 5.

divisivel = int(input('digite um numero>> '))

if divisivel % 3 == 0 and divisivel % 5 == 0:
    print('o numero é divisivel por 3 e 5')
else:
    print('o numero não é divisivel')
