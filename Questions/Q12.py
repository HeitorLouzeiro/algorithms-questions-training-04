'''

Write a program that receives five numbers and displays the following output:
Enter the 1st number 5
Enter the 2nd number 3
Enter the 3rd number 2
Enter the 4th number 0
Enter the 5th number 2
The numbers entered were: 5 + 3 + 2 + 0 + 2 = 12

'''
vetor = []

somaVetor = 0

for i in range(5):
    numero = int(input('Digite um numero: '))
    vetor.append(numero)
    somaVetor += numero

print(f'Os numeros digitados foram: {somaVetor}')
