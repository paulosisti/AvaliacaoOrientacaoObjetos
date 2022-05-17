# AvaliacaoOrientacaoObjetos

Primeira avaliação da disciplina de Algorítmos e Estruturas de Dados I com foco no paradígma de POO com Python.

## Desafio:
Construir o código necessário em Python para implementar o seguinte projeto:

O sistema possuirá uma classe abstrata chamada de Ferramenta que deve conter os atributos/propriedades nome, tensão e preço. Esta classe também deve possuir um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

O projeto também deve possuir as classes concretas, Furadeira e Lixadeira que herdam da classe Ferramenta.

A classe Furadeira deve possuir o atributo/propriedade fracamente privado, potência. Esta classe reimplementa o método getInformacoes() herdado de Furadeira.

A classe Lixadeira possui o atributo/propriedade fortemente privado, rotações. Esta classe reimplementa o método getInformacoes() herdado de Furadeira.

Construa um menu com as opções para cadastrar as ferramentas suportadas pelo sistema.
