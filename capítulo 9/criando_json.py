import json

produtos = {
    'PS5': {
        'ID':2022,
        'Valor':5000,
        'Quantidade': 100,
        },
    'God Of War Rangnarock': {
        'ID': 2023,
        'Valor': 250,
        'Quantidade':50
    }
}

with open('produtos.json','w') as meu_arquivo:
     json.dump(produtos, meu_arquivo)
with open('produtos.json','r') as arquivo:
    print(json.load(arquivo))