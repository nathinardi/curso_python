class Carro:

    def __init__(self,marca:str,modelo:str,ano:int,autonomia:int):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.autonomia=autonomia

    def liga_carro(self, ignicao = True):
        if ignicao:
            print(f'Seu {self.modelo} está ligado')
        else:
            print('Seu carro não está ligado')

    def calcula_autonomia(self, litros: int):
        """
        : param litros: Litros de gasolina que foram abastecidos
        : return: autonomia total
        """
        return litros * self.autonomia


meu_carro = Carro ('BMW', 'X6', 2023, 15)

print(meu_carro.marca)
print(meu_carro.modelo)
print(meu_carro.ano)

meu_carro.liga_carro()
print(meu_carro.calcula_autonomia(38))

