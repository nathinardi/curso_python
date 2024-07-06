idade = int(input("Entre com sua idade:"))
cnh = True

if idade >= 65:
    if cnh:
        print('Renove a carta a cada 5 anos')
    else:
        pass
elif 65 > idade >=18:
    if cnh:
        print ('Renove a carta a cada 10 anos')
    else: pass
else:
    print('Caso tenha interesse em tirar a carta, aguarde completar a idade mínima de 18 anos.')
