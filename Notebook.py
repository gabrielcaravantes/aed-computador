from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return f"Informações do notebook:\nNotebook de modelo {self.modelo}, de cor {self.cor}, com o preço de {self.preco:.2f} reais e bateria com o tempo de {self.__tempoDeBateria} horas.\n"
    
    def cadastrar(self, lista_notebooks):
        lista_notebooks.append(self)
        print(f"Foi cadastrado com sucesso um Notebook de modelo {self.modelo}, cor {self.cor} e tempo de bateria de {self.__tempoDeBateria} horas")
