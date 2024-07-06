#Escopo Global

def minha_func():
    print('minha primeira função!')

minha_func()

print(minha_func)


a = 42

def minha_funcao():

    global a
    a = 35

minha_funcao()

print(a)







