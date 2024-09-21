class Pessoa:
    def __init__(self, nome, idade, nacionalidade, religiao, ideologia):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.religiao = religiao
        self.ideologia = ideologia

    def __str__(self):
        return (f'Nome: {self.nome}\n'
                f'Idade: {self.idade}\n'
                f'Nacionalidade: {self.nacionalidade}\n'
                f'Religião: {self.religiao}\n'
                f'Ideologia: {self.ideologia}')

p1 = Pessoa("MIKE", 32, "Brasil", "budista", "facista")
print(p1)
