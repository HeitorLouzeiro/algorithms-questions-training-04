'''

Write a program that fills a vector with the names of seven students
and load another vector with the mean
end of these students. Calculate and show:
■■ the name of the student with the highest average (disregard ties);
■■ for each student who did not pass, that is, with an average of less than 7,
show how much this student needs to take on the test
final exam to be approved.
Consider that the average for passing the exam is 5.

'''

alunoVetor = []
mediaVetor = []
maiorMedia = float(0)
nomeMaiorMedia = ''

space = '-' * 50

for i in range(7):
    nome = input('Digite o nome do aluno: ')
    media = float(input('Digite a média do aluno: '))
    print(space)
    alunoVetor.append(nome)
    mediaVetor.append(media)

    if i == 0:
        maiorMedia = media
        nomeMaiorMedia = nome
    else:
        if media > maiorMedia:
            maiorMedia = media
            nomeMaiorMedia = nome

    if media < 7:
        faltaAprovar = 5 - (media * 0.6)
        print(
            f'O aluno {nome} precisa tirar {faltaAprovar:.2f} na prova final para ser aprovado')
        print(space)

print(f'O aluno com maior media é {nomeMaiorMedia} com a media {maiorMedia}')
