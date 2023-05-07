from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

lista_desktop = []
desktop = Desktop("Asus", "Preto", 8500.00, 750)
print(desktop.getInformacoes())
desktop.cadastrar(lista_desktop)

print("\n")

lista_notebooks = []
notebook = Notebook("Alienware", "Vermelho", 5500.00, 14)
print(notebook.getInformacoes())
notebook.cadastrar(lista_notebooks)
