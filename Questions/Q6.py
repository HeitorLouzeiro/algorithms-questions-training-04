'''

Write a program that receives the total sales of each salesperson in a store
and store them in a vector.
Also receive the commission percentage to which each seller is entitled
and store them in another vector.
Get the names of these sellers and store them in a third vector.
There are only ten sellers in
store. Calculate and show:
■■ a report with the names of sellers
    and the amounts receivable referring to the commission;
■■ the total sales of all salespeople;
■■ the largest amount to be received and the name of the person who will receive it;
■■ the smallest amount to be received and the name of the person who will receive it.

'''

nomesVetor = []
vendasVetor = []
comissaoVetor = []

totalVendas = float(0)
maiorValor = float(0)
menorValor = float(0)
maiorNome = ''
menorNome = ''

space = '-' * 50

for i in range(10):
    nome = input('Digite o nome do vendedor: ')
    nomesVetor.append(nome)
    vendas = float(input('Digite o total de vendas: '))
    vendasVetor.append(vendas)
    totalVendas += vendas
    comissao = float(input('Digite o percentual de comissão: '))
    print(space)
    comissaoVetor.append(comissao)

    # Calcula o valor a receber na comissão
    valorComissao = vendas * (comissao / 100)

    # Verifica se é o primeiro valor do vetor
    if i == 0:
        maiorValor = valorComissao
        menorValor = valorComissao
        maiorNome = nome
        menorNome = nome
    else:
        if valorComissao > maiorValor:
            maiorValor = valorComissao
            maiorNome = nome

        if valorComissao < menorValor:
            menorValor = valorComissao
            menorNome = nome

    print(space)
    print('Nome: ', nome)
    print('Valor a receber: ', valorComissao)
    print(space)

print('Total de vendas: ', totalVendas)
print('Maior valor a receber: ', maiorValor)
print('Nome do vendedor: ', maiorNome)
