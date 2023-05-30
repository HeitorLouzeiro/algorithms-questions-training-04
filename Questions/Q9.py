'''

Write a program that fills three vectors with ten positions each:
the first vector, with the names of
ten products; the second vector, with the codes of the ten products;
and the third vector, with the prices of the products.
Show a report with just the name, code,
the price and the new price of the products that will be increased.
It is known that the products that will suffer an increase are those that have
par code or price higher than
BRL 1,000.00. It is also known that, for products that satisfy
the two previous conditions, code and price, the increase will be 20%;
for those who satisfy only the code condition, the increase will be 15%;
and for those who satisfy only the price condition, the increase will be 10%.

'''
nomeVetor = []
codigoVetor = []
precoVetor = []

tam = 10

space = '-' * 50

for i in range(tam):
    nome = input('Digite o nome do produto: ')
    codigo = int(input('Digite o codigo do produto: '))
    preco = float(input('Digite o preço do produto: '))
    print(space)

    nomeVetor.append(nome)
    codigoVetor.append(codigo)
    precoVetor.append(preco)

for i in range(tam):
    if codigoVetor[i] % 2 == 0 and precoVetor[i] > 1000:
        novoPreco = precoVetor[i] * 1.2
    elif codigoVetor[i] % 2 == 0:
        novoPreco = precoVetor[i] * 1.15
    elif precoVetor[i] > 1000:
        novoPreco = precoVetor[i] * 1.1
    else:
        novoPreco = precoVetor[i]

    print('Nome: ', nomeVetor[i])
    print('Codigo: ', codigoVetor[i])
    print('Preço: ', precoVetor[i])
    print('Novo preço: ', novoPreco)
    print(space)
