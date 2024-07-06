#Operados Boleanos
#Unir condições lógicas ou avaliações

#print(2 == 2 and 3> 10)

#acesso = True
#credenciais = False

#print ( 'acesso and credenciais' )

#if acesso:
#   if credenciais:
#      print ('bem vindo')
#      else:
#    print ('Sai fora')


  # or

#print( 2 > 3 or 3 == 5 or 10 > 1 )
#print(12 > 3 or 3 == 5 or 10 > 1 and 3 % 2 == 0)

# print(not 3 ==3)

#sol = False
#calor =True

#if sol and calor:
#    print('Bora para praia!')
#elif sol and not calor:
#    print('Bora para o parque!')
#elif not sol and calor:
#    print('Bora para piscina.')
#elif not sol and not calor:
#    print ('Netflix')



a = int(input("medida do primeiro lado:"))
b= int(input("medida do segundo lado:"))
c= int(input("medida do terceiro lado:"))

if a + b > c or b + c > a or a + c > b:
    print("triangulo")
if a == b == c:
    print(" triangulo equilatero")
if a == b or b == c or a  == c:
    print("tiangulo isoceles")