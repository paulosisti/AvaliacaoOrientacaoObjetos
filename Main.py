from Ferramenta import Ferramenta
from Furadeira import Furadeira
from Lixadeira import Lixadeira

listaFuradeira = []
listaLixadeira = []

import os
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionarFuradeira():
  while True:
    furadeiraNome = input("Digite o nome da furadeira: ").upper()
    furadeiraTensao = input("Digite a tensão: ").upper()
    furadeiraPreco = input("Digite o preço: ").upper()
    furadeiraPotencia = input("Digite a potência: ").upper()
    if furadeiraNome:
      newFuradeira = Furadeira(furadeiraNome,furadeiraTensao,furadeiraPreco,furadeiraPotencia)
      listaFuradeira.append(newFuradeira)
      newFuradeira.cadastrar()
      break

def adicionarLixadeira():
  while True:
    lixadeiraNome = input("Digite o nome da lixadeira: ").upper()
    lixadeiraTensao = input("Digite a tensão: ").upper()
    lixadeiraPreco = input("Digite o preço: ").upper()
    lixadeiraRotacao = input("Digite as rotações: ").upper()
    if lixadeiraNome:
      newLixadeira = Lixadeira(lixadeiraNome,lixadeiraTensao,lixadeiraPreco,lixadeiraRotacao)
      listaLixadeira.append(newLixadeira)
      newLixadeira.cadastrar()
      break

def relatorioFuradeira():
  print("Relatório Furadeiras")
  print("--------------------")
  for furadeira in listaFuradeira:
    print(furadeira.getInformacoes())
    print("--------------------")

def relatorioLixadeira():
  print("Relatório Lixadeiras")
  print("--------------------")
  for lixadeira in listaLixadeira:
    print(lixadeira.getInformacoes())
    print("--------------------")







while True:
    
    print("""             
            MENU
    [0]	Finalizar o Programa
    [1]	Adicionar Furadeira
    [2]	Adicionar Lixadeira
    [3]	Relatório Furadeiras
    [4] Relatório Lixadeiras
        """)

    escolha = input("    Escolha uma opção: ")
    limpa_tela()

    if escolha == '0':
      print("Programa Encerrado!")
      break
    if escolha == '1':
      adicionarFuradeira()
    if escolha == '2':
      adicionarLixadeira()
    if escolha == '3':
      relatorioFuradeira()
    if escolha == '4':
      relatorioLixadeira()