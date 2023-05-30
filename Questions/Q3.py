'''
Write a program to control a company's stock of goods.
Initially, the program must fill two vectors with ten positions each,
where the first corresponds to the product code and the
second, to the total of that product in stock.
Soon after, the program should read an indeterminate set
of data containing the code of a customer
and the code of the product he wants to buy, along with the
amount. Customer code equal to zero indicates end of program.
The program should check:
■■ if the requested product code exists. If it exists,
try to fulfill the request; otherwise display
message Code does not exist;
■■ each order placed by a customer can only be filled in full.
If this is not possible,
write message We don't have enough stock of this product.
If I can help you, write
the Request Fulfilled message. Thank you and come back often;
■■ perform stock update only
    if the request is fulfilled in full;
■■ at the end of the program, write the product codes
    with their respective stocks already updated.
'''

codigos = []
estoque = []
space = '-' * 50

for i in range(10):
    codigos.append(int(input('Digite o codigo do produto: ')))
    estoque.append(int(input('Digite a quantidade do produto: ')))
    print(space)

codCliente = 1

while codCliente != 0:
    print('Digite 0 para sair.')
    codCliente = int(input('Digite o codigo do cliente: '))
    print(space)

    if codCliente == 0:
        break

    codProduto = int(input('Digite o codigo do produto: '))
    qtdProduto = int(input('Digite a quantidade do produto: '))
    print(space)

    for codigo in codigos:
        if codProduto == codigo:
            # pegando a posicao do codigo no vetor
            indice = codigos.index(codProduto)

            # estoque[indice] pega o valor do estoque que esta na mesma posicao do codigo
            # se o estoque for maior ou igual a quantidade do produto
            if estoque[indice] >= qtdProduto:
                estoque[indice] -= qtdProduto
                print('Pedido atendido. Obrigado e volte sempre.')

                print('Estoque atualizado:')
                # mostrando o estoque atualizado
                for i in range(len(codigos)):
                    print(f'Produto: {codigos[i]} - Estoque: {estoque[i]}')
            else:
                print('Não temos estoque suficiente dessa mercadoria.')
        else:
            print('Codigo inexistente.')

    print(space)
