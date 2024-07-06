with open('ana_julia.txt','r', encoding = 'utf-8') as file:


    for linha in file.readlines():

        if 'Anna' in linha:
            print(linha)



