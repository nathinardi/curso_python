class Pessoa:

    def __init__ (self,nome:str, idade:int):

        self.nome = nome
        sel.idade = idade

    def apresenta(self):

        print(f'Oi meu nome é {self.nome} e tenho {self.idade} anos.')

class Brasileiro(Pessoa):

    def __init__ (self, nome, idade, estado: str, cidade: str):
        super(). __init__ (nome.idade)
        self.estado = estado
        self.cidade = cidade

    def apresenta(self):
        super().apresenta()
        print(f'Sou de{self.cidade} / { self.estado}.')

