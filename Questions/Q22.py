'''
Write a program that reads a ten-position vector A.
Then compress the vector, removing null and negative values.
Store this result in vector B. Show vector B.
(Remember: vector B may not be completely filled.

'''

vetorA = []

vetorB = []

space = '-' * 50

for i in range(10):
    numero = int(input('Digite um número: '))

    vetorA.append(numero)

    if vetorA[i] > 0:
        vetorB.append(vetorA[i])
print(space)

print(vetorA)
print(vetorB)
