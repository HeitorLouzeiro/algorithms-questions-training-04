'''

Write a program that fills a vector with ten integers
and a second vector with five integers,
calculate and show two resultant vectors.

The first resulting vector will be composed by the sum of each number
even of the first vector added to all the numbers of the second vector.

The second resulting vector will be composed of the number of divisors
that each odd number in the first vector has in the second vector.

First
vector 4 7 5 8 2 15 9 6 10 11
1 2 3 4 5
1 2 3 4 5
3 4 5 8 2
6 7 8 9 10

Second
vector
First resultant vector Second resultant vector
26 30 …
8+3+4+5+8+2
4+3+4+5+8+2
0 1 …

7 does not have
dividers
24 2
15 is divisible
by 3 and by 5

'''

vetor1 = []
vetor2 = []

somaVetor = 0

vetor1Resultante = []
vetor2Resultante = []

space = '-' * 50


for i in range(10):
    numero = int(input('Digite um numero: '))
    vetor1.append(numero)
print(space)


for i in range(5):
    numero = int(input('Digite um para o segundo vetor: '))
    vetor2.append(numero)
print(space)


# Soma todos os numeros do vetor2
for numero in vetor2:
    somaVetor += numero

# Selecionando numeros pares
for numero in vetor1:
    if numero % 2 == 0:
        # Soma o numero par com a soma do vetor2
        vetor1Resultante.append(numero + somaVetor)

for numero in vetor1:
    # Selecionando numeros impares
    if numero % 2 != 0:
        divisor = 0
        # Selecionando numeros do vetor2
        for numero2 in vetor2:
            # Verificando se o numero do vetor1 é divisivel pelo numero do vetor2

            # se o numero2 for diferente de 0 e o resto da divisao for 0
            if numero2 != 0 and numero % numero2 == 0:
                # Se for divisivel, adiciona 1 ao divisor
                divisor += 1

        # Adiciona o divisor ao vetor2Resultante
        vetor2Resultante.append(divisor)

print(f'Resultado do primeiro vetor: {vetor1Resultante}')
print(f'Resultado do segundo vetor: {vetor2Resultante}')
