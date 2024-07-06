

#media_alunos
#
#
# alunos = {'Joao': [ 7,4,5], 'Maria': [ 5,8,9],
#           'Leo': [6,7,7],'Pedro': [7,4,10]}
#
# alunos_medias = list(map(lambda notas: round(sum(notas) / len(notas), 2),
#                          alunos.values ()))
#
# print(alunos_medias)
#
# for nome, media in alunos_medias:
#     print(f'Aluno: {alunos} - Média: {alunos_medias}')
#
#
# alunos_medias = {nome: round(sum(notas) / len(notas), 2) for nome, notas in alunos.items()}
#
# # Exibindo o nome do aluno junto com a média
# for nome, notas in alunos_medias.items():
#     print(f'Aluno: {alunos} - Média: {alunos_medias}')



alunos = {'Joao': [7, 4, 5], 'Maria': [5, 8, 9],
          'Leo': [6, 7, 7], 'Pedro': [7, 4, 10]}

# Calculando as médias dos alunos
alunos_medias = {nome: round(sum(notas) / len(notas), 2) for nome, notas in alunos.items()}

# Exibindo o nome do aluno junto com a média
for nome, media in alunos_medias.items():
    print(f'Aluno: {nome} - Média: {media}')






