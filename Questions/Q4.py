'''
Write a program that fills a vector with fifteen integer elements
and check for elements
equal to 30, showing the positions in which they appeared.

'''

vetor = []
posicaoVetor = []

space = '-' * 50

for i in range(15):
    numero = int(input('Digite um numero: '))
    vetor.append(numero)
    print(space)

for i in range(len(vetor)):
    # se o numero for igual a 30
    if vetor[i] == 30:
        # pegando a posicao do numero 30 no vetor
        posicaoVetor.append(i)
print(space)
print(f'O numero 30 apareceu na posicao {posicaoVetor}')
