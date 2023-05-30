'''

Write a program that reads a vector with fifteen positions for integers.
After reading, divide all of its elements by the largest vector value.
Show the vector after the calculations.

'''

vetor = []
vetorResultante = []

maiorNumero = float(0)

space = '-' * 50

for i in range(5):
    numero = int(input('Digite um número inteiro: '))
    vetor.append(numero)

    if numero > maiorNumero:
        maiorNumero = numero

for i in vetor:
    div = i / maiorNumero
    vetorResultante.append(div)

print(space)
print(f'O maior número do vetor é {maiorNumero}')
print(space)

print(f'Resultado da divisão: {vetorResultante}')
