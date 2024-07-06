senha = input('Cadastre uma senha de 6 dígitos:\n')

while True:
    if len(senha) != 6:
        senha = input('Quantidade de char inválida \n'
                      'Cadastre uma senha de 6 dígitos: \n')
        continue
    else:
        break

print('Senha cadastrada com sucesso')

