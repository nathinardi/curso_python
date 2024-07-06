import matplotlib.pyplot as plt

linguagens = ['C++', 'C#', 'Phyton','Java','Go']
votos = [100,150,350,50,65]

plt.bar(linguagens,votos, color='#820000', align='edge', width = 0.1)
plt.title('Linguagens de programação x Quantidade de votos')
plt.xlabel('Linguagens de programação')
plt.ylabel('Votos por linguagem')

#plt.bar(linguagens,votos)
plt.show()

