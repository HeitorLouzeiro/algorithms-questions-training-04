'''

Make a program that receives the name and two grades of six students
and show the following report. Report
of notes:
STUDENT 1st
 TEST 2a
 SITUATION AVERAGE EXAM
Carlos 8.0 9.0 8.5 Approved
Peter 4.0 5.0 4.5 Failed
■■ class average = ?
■■ percentage of approved students = ?%
■■ percentage of exam students = ?%
■■ percentage of students who failed = ?%

'''

vetorNome = []

vetorNota1 = []
vetorNota2 = []

vetorMedia = []

situacao = []

somaNota1 = float(0)
somaNota2 = float(0)

mediaClasse = float(0)

space = '-' * 50

for i in range(4):
    nome = input('Digite o nome do aluno:')
    vetorNome.append(nome)

    nota1 = float(input('Digite a nota da prova 1: '))
    vetorNota1.append(nota1)

    nota2 = float(input('Digite a nota da prova 2: '))
    vetorNota2.append(nota2)

    somaNota1 += nota1
    somaNota2 += nota2

    media = (nota1 + nota2) / 2
    mediaClasse += media

    vetorMedia.append(media)
    if media >= 7:
        situacao.append('Aprovado')
    elif media >= 4:
        situacao.append('Exame')
    else:
        situacao.append('Reprovado')

    print(space)

mediaTotalClasse = mediaClasse / len(vetorMedia)

print('Relatório de Notas: ')
for aluno in range(len(vetorNome)):
    print(f'Aluno {vetorNome[aluno]}')
    print(f'Prova 1 = {vetorNota1[aluno]}')
    print(f'Prova 2 = {vetorNota2[aluno]}')
    print(f'Média = {vetorMedia[aluno]}')
    print(f'Situação = {situacao[aluno]}')
    print(space)


print(f'Media da Classe = {mediaTotalClasse}')

porcentAprovados = situacao.count('Aprovado') * 100 / len(situacao)
porcentExame = situacao.count('Exame') * 100 / len(situacao)
porcentReprovados = situacao.count('Reprovado') * 100 / len(situacao)

print(f'Porcentagem de Aprovados = {porcentAprovados}%')
print(f'Porcentagem de Exame = {porcentExame}%')
print(f'Porcentagem de Reprovados = {porcentReprovados}%')
