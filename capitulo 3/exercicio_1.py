nome = input("Entre com seu nome:").title()
nota_P1 = int(input('Entre com sua nota p1:'))
nota_P2 = int(input('Entre com sua nota p2:'))

media = (nota_P2 + nota_P1) / 2

if media == 10:
   print (f'Sua média foi de {media} Aprovado com Distinção!')
elif media >= 7 :
   print(f'Sua média foi de {media} Aprovado.')
else:
   print(f'Sua média foi de {media} Reprovado.')




