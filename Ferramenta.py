from abc import ABCMeta, abstractmethod

class Ferramenta(metaclass = ABCMeta):

  def __init__(self, nome, tensao, preco):
    self.nome = nome
    self.tensao = tensao
    self.preco = preco 

  def getInformacoes(self):
    return print(f"Ferramenta: {self.nome} \nTensão: {self.tensao} \nPreço: {self.preco}")

  @abstractmethod
  def cadastrar(self):
    pass