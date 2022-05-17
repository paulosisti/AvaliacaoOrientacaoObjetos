from Ferramenta import Ferramenta

class Furadeira(Ferramenta):

  def __init__(self,  nome, tensao, preco, potencia):
      super().__init__(nome, tensao, preco)
      self._potencia = potencia

  def getInformacoes(self):
    super().getInformacoes()
    return f"Potência: {self._potencia}"
  
  def cadastrar(self):
    return print(f"Furadeira Cadastrada com Sucesso!")