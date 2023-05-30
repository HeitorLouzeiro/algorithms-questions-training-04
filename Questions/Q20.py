'''

Write a program that reads a vector with ten positions for integers
and show only positive numbers.

'''

vetor = []

for i in range(10):
    numero = int(input('Digite um número: '))
    vetor.append(numero)

for i in vetor:
    if i > 0:
        print(f'Numeros positivos: {i}')
