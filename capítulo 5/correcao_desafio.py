#todo: Receber os itens e armazenar na lista

lista= []

while True:
      item = input('Entre com um dado( ou enter para sair):')
      if item:
          lista.append(item)
          continue
      else:
          break


print(lista)

#TODO: Eliminar itens repetidos

lista_nova = list(set (lista))

print(lista_nova)

#todo: Ordenar a lista

lista_nova.sort()

print(lista_nova)

