import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
servicos = np.random.random(10) *100
manutencao = np.random.random(10) *100

#plt.figure(1)

plt.plot(servicos, label='serviços_1',c="green")
#plt.legend(loc = 'upper center')

#plt.figure(2)
plt.plot(manutencao, 'r--', label='empresa2')
plt.legend(loc='upper center')

plt.show()