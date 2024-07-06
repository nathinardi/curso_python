class Animal:

    def __init__ (self,raça:str, peso:int):

        self.nome = raça
        sel.idade = peso

    def apresenta(self):

        print(f'Oi eu tenho um cachorro da raça {self.raça} e ele pesa {self.peso} kg.')

class Cachorro(Animal):

    def __init__ (self, raça: str, peso:int, nome: str, cor: str):
        super(). __init__ (raça,peso)
        self.nome = nome
        self.cor = cor

    def apresenta(self):
        super().apresenta()
        print(f'As características do meu cachorro são {self.nome} / { self.cor}.')

class Gato(Animal):
    def __init__ (self, raça: str, peso:int, nome: str, cor: str):
        super(). __init__ (raça,peso)
        self.nome = nome
        self.cor = cor

    def apresenta(self):
        super().apresenta()
        print(f'As características do meu gato são {self.nome} / { self.cor}.')




meu_cachorro = Cachorro('Labrador', 25, 'Rex', 'Dourado')
meu_gato = Gato('Siames', 5, 'Miau', 'Branco')

print(meu_gato.nome)



