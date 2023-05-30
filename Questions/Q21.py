'''
Write a program that reads a vector with ten positions for integers.
Create a second vector, replacing null values ​​with 1.
Show the two vectors.

'''

vetor = []

vetor2 = []
space = '-' * 50

for i in range(10):
    numero = int(input("Digite um numero: "))
    vetor.append(numero)

    if numero == 0:
        vetor2.append(1)
    else:
        vetor2.append(numero)

print(space)
print(vetor)
print(vetor2)
