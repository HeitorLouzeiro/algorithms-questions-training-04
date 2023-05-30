'''

Write a program that fills a vector with fifteen numbers, determines and displays:
■■ the largest number and its position in the vector;
■■ the smallest number and its position in the vector.

'''

vetor = []

posicao_maior = 0

posicao_menor = 0

space = '-' * 50

for i in range(4):
    numero = int(input('Digite um número: '))
    vetor.append(numero)

    if i == 0:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero
        posicao_maior = i

    if numero < menor:
        menor = numero
        posicao_menor = i

print(space)

print(f'O maior número é: {maior} e a posição dele é: {posicao_maior}')
print(f'O menor número é: {menor} e a posição dele é: {posicao_menor}')
