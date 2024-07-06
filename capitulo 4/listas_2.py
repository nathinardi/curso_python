quantidade_itens = int(input('Quantidade de itens que você deseja adicionar na sua lista de mercado:'))

Lista_mercado : []

for i in range(quantidade_itens):
    nome_item = input(f"Digite o nome do item {i+1}: ")
    lista_mercado.append(nome_item)

print("\nLista de mercado:")
for item in lista_mercado:
    print(item)
