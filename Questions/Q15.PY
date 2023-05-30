'''
Write a program that receives the names of eight customers and stores them in an array.
In a second array, store the number of DVDs rented in 2011 by each of the eight customers.
It is known that for every ten leases, the customer is entitled to one free lease.
Make a program that shows the name of all customers,
with the amount of free rentals to which he is entitled.

'''

vetorNome = []
vetorLocacoes = []
vetorLocacoesGratis = []

space = '-' * 50

for i in range(2):
    nome = input('Digite o nome do cliente: ')
    vetorNome.append(nome)

    locacoes = int(input('Digite a quantidade de locações: '))
    vetorLocacoes.append(locacoes)

    locacaoesGratis = locacoes // 10
    vetorLocacoesGratis.append(locacaoesGratis)
    print(space)

for i in range(len(vetorNome)):
    print(f'{vetorNome[i]} tem {vetorLocacoesGratis[i]} locações grátis.')
