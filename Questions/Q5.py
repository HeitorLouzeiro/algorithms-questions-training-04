'''

A school wants to know if there are students simultaneously studying
the disciplines Logic and Language of
Schedule.
Put the registration numbers of students who study Logic,
in a vector fifteen students.
Insert the enrollment numbers of the students who are studying
Programming Language in another vector, ten
students. Show the number of license plates that appear in the two vectors.

'''
vetorLogica = []
vetorLinguagem = []

vetorLogicaLinguagem = []

space = '-' * 50

for i in range(15):
    matriculaLogica = int(
        input('Digite o numero da matricula do aluno que cursa Logica: '))
    vetorLogica.append(matriculaLogica)
print(space)


for i in range(10):
    matriculaLinguagem = int(
        input('Digite o numero da matricula do aluno que cursa Linguagem: '))
    vetorLinguagem.append(matriculaLinguagem)
    print(space)
# For para percorrer o vetorLogica
for i in range(len(vetorLogica)):
    # For para percorrer o vetorLinguagem
    for j in range(len(vetorLinguagem)):
        '''
        se o numero da matricula do aluno que cursa Logica for igual
        ao numero da matricula do aluno que cursa Linguagem adicione
        no vetor vetorLogicaLinguagem
        '''
        if vetorLogica[i] == vetorLinguagem[j]:
            vetorLogicaLinguagem.append(vetorLogica[i])

print('Os alunos que cursam Logica e Linguagem sao:', vetorLogicaLinguagem)
print(space)
