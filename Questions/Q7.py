'''
Write a program that fills a vector with ten real numbers, calculates and
show the number of numbers
negatives and the sum of the positive numbers in that vector.

'''

vetor = []
negativos = 0
positivos = int(0)

space = '-' * 50

for i in range(10):
    numero = int(input('Digite um número: '))
    vetor.append(numero)
    print(space)

    if numero < 0:
        negativos += 1
    else:
        positivos += numero

print('Quantidade de números negativos: ', negativos)
print('Soma dos números positivos: ', positivos)
print(space)
