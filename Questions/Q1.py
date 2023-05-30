'''
Write a program that fills a vector with six integer elements.
Calculate and show:
■■ all even numbers;
■■ the number of even numbers;
■■ all odd numbers;
■■ the number of odd numbers.

'''

vetor = []
pares = []
impares = []
space = '-' * 50
for i in range(6):
    numero = int(input('Digite um numero: '))
    vetor.append(numero)
    print(space)

for i in vetor:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Os numeros pares são: {pares}')
print(f'Os numeros impares são: {impares}')
print(f'A quantidade de numeros pares é: {len(pares)}')
print(f'A quantidade de numeros impares é: {len(impares)}')
print(space)
