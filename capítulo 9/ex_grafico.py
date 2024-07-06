import matplotlib.pyplot as plt
import mplcursors
import plotly.graph_objects as go

# Dados de exemplo
codigos = ['QA123', 'QA321']
volumetria = [10, 15]
labels = ['contrato', 'cartão']

# Criando o gráfico de barras
fig, ax = plt.subplots()
bars = ax.bar(codigos, volumetria)

# Adicionando a interatividade com mplcursors
cursor = mplcursors.cursor(ax, hover=True)
cursor.connect('add', lambda sel: sel.annotation.set_text(f'{labels[sel.target.index]}'))

# Configurações adicionais do gráfico
ax.set_xlabel('Códigos')
ax.set_ylabel('Volumetria')
ax.set_title('Gráfico de Barras Interativo')

plt.show()

fig.write_html('grafico_interativo.html')
