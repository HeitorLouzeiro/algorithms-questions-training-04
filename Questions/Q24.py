'''

Write a program that reads a vector with fifteen positions for integers.
Then create a resultant vector that contains
all prime numbers in the entered array. Write the resulting vector.

'''

vetor = []
vetorResultante = []

space = '-' * 50

for i in range(5):
    numero = int(input('Digite um número inteiro: '))
    vetor.append(numero)

for i in vetor:
    if i > 1:
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break

        if primo:
            vetorResultante.append(i)

print(space)

print(f'Os numeros que são primos {vetorResultante}')
