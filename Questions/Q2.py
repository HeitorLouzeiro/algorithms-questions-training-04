'''

Write a program that fills a vector with seven integers,
calculate and show:
■■ numbers that are multiples of 2;
■■ numbers that are multiples of 3;
■■ numbers that are multiples of 2 and 3.

'''
vetor = []
mult2 = []
mult3 = []
mult2e3 = []

space = '-' * 50
for i in range(7):
    numero = int(input('Digite um numero: '))
    vetor.append(numero)
    print(space)

for i in vetor:
    if i % 2 == 0:
        mult2.append(i)
    if i % 3 == 0:
        mult3.append(i)
    if i % 2 == 0 and i % 3 == 0:
        mult2e3.append(i)

print(f'Os numeros multiplos de 2 são: {mult2}')
print(f'Os numeros multiplos de 3 são: {mult3}')
print(f'Os numeros multiplos de 2 e 3 são: {mult2e3}')
print(space)
