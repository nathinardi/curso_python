lista_pares =  [n for n in range(0,51) if n % 2 == 0 ]

print(lista_pares)


alunos_notas = {'João': [7,4,5], 'Maria': [5,8,9],
                'Leo': [6,7,7], 'Pedro': [7,4,10]}

aprovados = [aluno[0] for aluno in alunos_notas.items()
    if round(sum(aluno[1])/len(aluno[1]),2) >= 7]

print(aprovados)



#len retorna a quantidade de itens
#sum soma a quantidade de valores

