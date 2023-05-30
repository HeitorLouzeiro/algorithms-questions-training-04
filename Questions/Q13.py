'''
Write a program that receives the names and grades of eight students
and show the following report:
Enter the name of the 1st
 student: Charles
Enter Carlos' grade: 8
Enter the name of the 2nd
 student: peter
Enter Pedro's grade: 5
grade reports
Charles 8.0
Peter 5.0
..
..
..
Class average = ??

'''

vetorNome = []
vetorNota = []

somaNota = float(0)

for i in range(8):
    nome = input('Digite o nome do aluno:')
    vetorNome.append(nome)
    nota = float(input('Digite a nota do aluno: '))
    vetorNota.append(nota)
    somaNota += nota

media = somaNota / len(vetorNota)


print(f'Media da Classe = {media}')
