'''

Write a program that takes ten integers and stores them in a vector.
Calculate and show two

resulting vectors: the first with the even numbers and the second,
with odd numbers.

'''

vetor = []
vetorPar = []
vetorImpar = []

for i in range(10):
    numero = int(input('Digite um numero: '))
    vetor.append(numero)

for numero in vetor:
    if numero % 2 == 0:
        vetorPar.append(numero)
    else:
        vetorImpar.append(numero)

print('Vetor: ', vetor)

print('Numeros Par: ', vetorPar)

print('Numeros Impar: ', vetorImpar)
