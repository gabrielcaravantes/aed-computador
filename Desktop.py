from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"Informações do Desktop\nDesktop de modelo {self.modelo}, de cor {self.cor}, com o preço de {self.preco:.2f} reais e fonte com {self._potenciaDaFonte} watts de potência.\n"

    def cadastrar(self, lista_desktop):
        lista_desktop.append(self)
        print(f"Foi cadastrado com sucesso um Desktop de modelo {self.modelo}, de cor {self.cor}, com o preço de {self.preco:.2f} e fonte com {self._potenciaDaFonte} watts de potência.")
