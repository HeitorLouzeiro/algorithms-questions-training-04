'''

Make a program that fills two vectors of ten positions each,
determine and show a third containing the elements
of the two previous vectors sorted in descending order

'''

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(4):
    numero = int(input('Digite um número para o primeiro vetor: '))
    vetor1.append(numero)

    numero2 = int(input('Digite um número para o segundo vetor: '))
    vetor2.append(numero2)

    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

for i in range(len(vetor3)):
    for j in range(i+1, len(vetor3)):
        # Verifica se o elemento atual é maior que o próximo
        if vetor3[i] < vetor3[j]:
            '''
            Atribuimos o valor do elemento atual a uma variável auxiliar,
            para que não seja perdido na hora da troca.
            '''
            aux = vetor3[i]
            # O elemento atual recebe o valor do próximo
            vetor3[i] = vetor3[j]
            # O próximo elemento recebe o valor do atual
            vetor3[j] = aux
print(vetor3)

'''

Primeiro laço for percorre o vetor3, e o segundo laço for percorre o vetor3
exemplo:
vetor3 = [7, 3, 9, 5, 2, 8, 4, 6]

primeira iteração: i = 0, j = 1
vetor3[i] = 7
vetor3[j] = 3
vetor3[i] < vetor3[j] ? 7 < 3 ? Não

segunda iteração: i = 0, j = 2
vetor3[i] = 7
vetor3[j] = 9

vetor3[i] < vetor3[j] ? 7 < 9 ? Sim

vetor3[i] = 9
vetor3[j] = 7

.
.
.
decima iteração: i = 0, j = 10



'''
