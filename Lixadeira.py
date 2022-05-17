from Ferramenta import Ferramenta

class Lixadeira(Ferramenta):

  def __init__(self,  nome, tensao, preco, rotacoes):
      super().__init__(nome, tensao, preco)
      self.__rotacoes = rotacoes

  def getInformacoes(self):
    super().getInformacoes()
    return f"Rotacoes: {self.__rotacoes}"
  
  def cadastrar(self):
    return print(f"Lixadeira Cadastrada com Sucesso!")