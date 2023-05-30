'''

Write a program that reads two vectors of ten positions and
multiply the same elements
index, placing the result in a third vector. Show the resulting vector.

'''

vetor1 = []
vetor2 = []

vetorResultante = []

space = '-' * 50

for i in range(10):
    numero = int(input('Digite um número: '))
    vetor1.append(numero)

    numero = int(input('Digite um número para ser multiplicado: '))
    vetor2.append(numero)

    vetorResultante.append(vetor1[i] * vetor2[i])
    print(space)

print(vetor1)
print(space)

print(vetor2)
print(space)

print(vetorResultante)
print(space)
