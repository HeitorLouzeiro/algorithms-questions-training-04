'''

Write a program that is named after five products
and their respective prices. Calculate and show:
■■ the number of products priced below R$50.00;
■■ the name of products priced between R$50.00 and R$100.00;
■■ the average price of products priced over R$100.00.
'''

vetorProduto = []
vetorPreco = []

vetorPrecoInferior = []
vetorPrecoEntre = []
vetorMediaSuperior = []

media = float(0)

for i in range(5):
    produto = input('Digite o nome do produto: ')
    vetorProduto.append(produto)

    preco = float(input('Digite o preço do produto: '))
    vetorPreco.append(preco)

    if vetorPreco[i] < 50:
        vetorPrecoInferior.append(vetorProduto[i])
    elif vetorPreco[i] >= 50 and vetorPreco[i] <= 100:
        vetorPrecoEntre.append(vetorProduto[i])
    else:
        vetorMediaSuperior.append(vetorPreco[i])
        media += vetorPreco[i]


mediaProduto = media / len(vetorMediaSuperior)

print(f'Produtos com preço inferior a R$ 50,00: {len(vetorPrecoInferior)}')
print(f'Produtos com preço entre R$ 50,00 e R$ 100,00: {vetorPrecoEntre}')
print(
    f'Produtos media dos produtos com preço superior a R$ 100,00: {mediaProduto}')
