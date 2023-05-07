from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        return f"Computador de modelo {self.modelo}, de cor {self.cor} e preço de {self.preco:.2f} reais."
    
    @abstractmethod
    def cadastrar(self):
        pass
