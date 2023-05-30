'''

Write a program that reads two vectors (A and B)
with five positions for whole numbers. The program must then
subtract the first element of A from the last of B, accumulating the value,
subtract the second element of A from the penultimate element of B,
accumulating the value and so on.
At the end, show the result of all subtractions performed

'''

vetorA = []

vetorB = []

resultado = 0

for i in range(5):
    numero = int(input('Digite um número para ser subtraido: '))
    vetorA.append(numero)

    numero = int(input('Digite um segundo número para ser subtraido: '))
    vetorB.append(numero)

for i in range(5):
    resultado += vetorA[i] - vetorB[5 - 1 - i]


print(vetorA)
print(vetorB)
print(resultado)

'''

resultado = 0
resultado += vetorA[0] - vetorB[4]
.
.
.
resultado += vetorA[4] - vetorB[0]

print(resultado)

'''
